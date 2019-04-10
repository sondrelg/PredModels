from bs4 import BeautifulSoup as bs
from aioify import aioify
import urllib.request
import pandas as pd
import requests
import asyncio
import re

def get_stock_history_tsv(ticker: str) -> dict:
    """
    Only takes tickers from OSE
    """
    # url = "https://cdn.rawgit.com/rrag/react-stockcharts/master/docs/data/MSFT.tsv"
    # df = pd.read_csv(response,sep="\t", index_col='date')

    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)
    df = pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")
    df = df[['quote_date', 'open', 'high', 'low', 'close', 'volume']]
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    jsn = [
        {"date": df.iloc[i]['date'], 'open': df.iloc[i]['open'], 'high': df.iloc[i]['high'], 'low': df.iloc[i]['low'],
         'close': df.iloc[i]['close'], 'volume': df.iloc[i]['volume']} for i in range(len(df.date))]
    jsn = jsn[::-1]
    return jsn


def get_stock_history(ticker: str) -> dict:
    """
    Only takes tickers from OSE
    """
    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)
    df = pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")
    return {'date': list(df['quote_date']), 'open': list(df['open']), 'high': list(df['high']), 'low': list(df['low']),
            'close': list(df['close']), 'volume': list(df['volume']), 'value': list(df['value']),
            'exch': list(df['exch'])}


def get_stock_history_async(ticker: str) -> dict:
    df = get_stock_history(ticker)
    return {ticker: [{'date': list(df['quote_date']),
                      'open': list(df['open']),
                      'high': list(df['high']),
                      'low': list(df['low']),
                      'close': list(df['close']),
                      'volume': list(df['volume']),
                      'value': list(df['value']),
                      'exch': list(df['exch'])}]}


def get_stock_histories(tickers: list) -> dict:
    """
    Takes a list of tickers from OSE
    """
    tasks, product = [], {}

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    for ticker in tickers:
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


def mock_endpoint() -> dict:
    # Get a handful of tickers
    tickers = get_stock_tickers()

    # Get data async
    tasks, product = [], {}
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for ticker in tickers[40:80]:
        task = asyncio.ensure_future(aioify(scrape_data)(ticker))
        tasks.append(task)
    responses = asyncio.gather(*tasks)
    product['results'] = loop.run_until_complete(responses)
    results = [i[next(iter(i))] for i in product['results']]
    return results


def scrape_data(ticker):
    # Get return
    response = requests.get(f'https://www.netfonds.no/quotes/ppaper.php?paper={ticker}.OSE')
    soup = bs(response.text, 'lxml')
    change = float(soup.find("td", {"name": "ju.cp"}).text.replace('%',''))
    level = str(change)[0]+"%"

    # Get name and value
    response = requests.get(f'https://www.netfonds.no/quotes/about.php?paper={ticker}.OSE')
    soup = bs(response.text, 'lxml')
    try:
        value = int(soup(text=re.compile(r'^Markedsverdi$'))[0].parent.parent.find('td').text.replace(' ', ''))
    except:
        value = 0
    name = soup(text=re.compile(r'^Navn$'))[0].parent.parent.find('td').text

    return {ticker: {'ticker': ticker, 'name': name, 'change': change, 'value': value, 'level':level}}
