from bs4 import BeautifulSoup as bs
from aioify import aioify
import urllib.request
import pandas as pd
import requests
import asyncio
import re


def get_stock_tickers() -> list:
    url = "http://www.netfonds.no/quotes/kurs.php"
    resp = requests.get(url)
    soup = bs(resp.text, 'lxml')
    table = soup.find('table', {'class': 'mbox'})
    tickers = [row.findAll('td')[1].text for row in table.findAll('tr')[1:] if row.findAll('td')[1].text[:3] != "OBX"]
    return tickers


def get_name_and_value(ticker):
    response = requests.get(f'https://www.netfonds.no/quotes/about.php?paper={ticker}.OSE')
    soup = bs(response.text, 'lxml')

    try:
        name = soup(text=re.compile(r'^Navn$'))[0].parent.parent.find('td').text
    except Exception as e:
        print(f'Failed getting name for {ticker}')
        name = None

    try:
        shares_outstanding = int(soup(text=re.compile(r'^Antall aksjer$'))[0].parent.parent.find('td').text.replace(' ', ''))
    except Exception as e:
        print(f'Failed getting value for {ticker}')
        shares_outstanding = None

    return {
            'ticker': ticker,
            'name': name,
            'shares_outstanding': shares_outstanding
            }

def get_data():
    tasks, data, tickers = [], {}, get_stock_tickers()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    for ticker in tickers:
        task = asyncio.ensure_future(aioify(get_name_and_value)(ticker))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    data = loop.run_until_complete(responses)

    return data
