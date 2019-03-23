from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import requests
import asyncio
from aioify import aioify


def get_stock_history(ticker: str) -> pd.DataFrame:
    """
    Only takes tickers from OSE
    """
    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)
    df = pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")
    return df


def get_stock_history_async(ticker: str) -> dict:
    df = get_stock_history(ticker)
    return {'ticker': df}


def get_stock_histories(tickers: list) -> dict:
    """
    Takes a list of tickers from OSE
    """
    tasks, product = [], {}

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    for ticker in tickers:
        print(ticker)
        task = asyncio.ensure_future(aioify(get_stock_history_async)(ticker))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    product['results'] = loop.run_until_complete(responses)
    return product


def get_stock_tickers() -> list:
    url = "http://www.netfonds.no/quotes/kurs.php"
    resp = requests.get(url)
    soup = bs(resp.text, 'lxml')
    table = soup.find('table', {'class': 'mbox'})
    tickers = [row.findAll('td')[1].text for row in table.findAll('tr')[1:] if row.findAll('td')[1].text[:3] != "OBX"]
    return tickers


