from bs4 import BeautifulSoup as bs
from aioify import aioify
import requests
import asyncio
import re

from data.models import Stocks


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
        if name == '':
            name = soup(text=re.compile(r'^Navn$'))[0].parent.parent.parent.find('th').text
            name = name.replace(f'Informasjon om ({ticker.upper()}) ', '')
    except Exception as e:
        print(f'Failed getting name for {ticker}')
        name = None

    try:
        shares_outstanding = soup(text=re.compile(r'^Antall aksjer$'))[0].parent.parent.find('td').text.replace(' ', '')
        if shares_outstanding != '' and shares_outstanding != '\xa0':
            shares_outstanding = int(shares_outstanding)
        else:
            shares_outstanding = None
    except Exception as e:
        print(f'Failed getting value for {ticker}')
        shares_outstanding = None

    return {'ticker': ticker,
            'name': name,
            'shares_outstanding': shares_outstanding}


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


def save_stocks(data):
    for datum in data:
        try:
            stock = Stocks.objects.get(ticker=datum['ticker'])
            if stock.name != datum['name']:
                stock.name = datum['name']
            if stock.shares_outstanding != datum['shares_outstanding']:
                stock.shares_outstanding = datum['shares_outstanding']
            stock.save()
            print(f"Updated {datum['ticker']}")
        except:
            try:
                Stocks.objects.create(ticker=datum['ticker'],
                                      name=datum['name'],
                                      shares_outstanding=datum['shares_outstanding'])
                print(f"Created {datum['ticker']}")
            except Exception as e:
                print(f"Failed saving {datum['ticker']}", e)