from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import requests
import asyncio
from aioify import aioify
import tsv

def get_stock_history_tsv(ticker: str) -> dict:
    """
    Only takes tickers from OSE
    """
    # url = "https://cdn.rawgit.com/rrag/react-stockcharts/master/docs/data/MSFT.tsv"
    # df = pd.read_csv(response,sep="\t", index_col='date')

    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)
    df = pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")
    df = df[['quote_date','open','high','low','close','volume']]
    df.columns = ['date','open','high','low','close','volume']
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    jsn = [{"date":df.iloc[i]['date'], 'open':df.iloc[i]['open'], 'high':df.iloc[i]['high'],'low':df.iloc[i]['low'],
            'close':df.iloc[i]['close'],'volume':df.iloc[i]['volume']} for i in range(len(df.date))]
    jsn = jsn[::-1]
    return jsn

def get_stock_history(ticker: str) -> dict:
    """
    Only takes tickers from OSE
    """
    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)
    df = pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")
    return {'date':list(df['quote_date']), 'open':list(df['open']), 'high':list(df['high']), 'low':list(df['low']),
           'close':list(df['close']), 'volume':list(df['volume']), 'value':list(df['value']), 'exch':list(df['exch'])}


def get_stock_history_async(ticker: str) -> dict:
    df = get_stock_history(ticker)
    return {ticker: [{'date':list(df['quote_date']),
                       'open':list(df['open']),
                       'high':list(df['high']),
                       'low':list(df['low']),
                       'close':list(df['close']),
                       'volume':list(df['volume']),
                       'value':list(df['value']),
                       'exch':list(df['exch'])}]}


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
