from bs4 import BeautifulSoup as bs
from aioify import aioify
import requests
import asyncio

from ..models import Stocks, CurrentData


def clean(s):
    s = s.replace(' ', '')
    if s == '-' or s == '':
        return None
    try:
        return float(s)
    except Exception as e:
        print('Error cleaning: %s', e)


def clean_int(s):
    s = s.replace(' ', '')
    if s == '-' or s == '':
        return None
    try:
        return int(s)
    except Exception as e:
        print('Error cleaning int: %s', e)


def get_stock(ticker: str) -> dict:
    response = requests.get(f'https://www.netfonds.no/quotes/ppaper.php?paper={ticker}.OSE')
    soup = bs(response.text, 'lxml')
    abs_change = clean(soup.find('td', {'name': 'ju.c'}).text)
    pct_change = clean(soup.find('td', {'name': 'ju.cp'}).text.replace('%', ''))
    opn = clean(soup.find('td', {'name': 'ju.op'}).text)
    high = clean(soup.find('td', {'name': 'ju.h'}).text)
    low = clean(soup.find('td', {'name': 'ju.lo'}).text)
    current = clean(soup.find('td', {'name': 'ju.l'}).text)
    previous = clean(soup.find('td', {'name': 'ju.pr'}).text)
    volume = clean_int(soup.find('td', {'name': 'ju.vo'}).text.replace(' ', ''))
    value = clean_int(soup.find('td', {'name': 'ju.va'}).text.replace(' ', ''))
    trades = clean_int(soup.find('td', {'name': 'ju.t'}).text.replace(' ', ''))
    return {f'{ticker}':
                {'change': abs_change,
                 'percent_change': pct_change,
                 'open': opn,
                 'high': high,
                 'low': low,
                 'current': current,
                 'previous': previous,
                 'volume': volume,
                 'value': value,
                 'trades': trades
                 }
            }

def get_data() -> dict:
    tickers = [ticker['ticker'] for ticker in Stocks.objects.values('ticker')]
    tasks, product, loop = [], {}, asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    for ticker in tickers:
        task = asyncio.ensure_future(aioify(get_stock)(ticker))
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    results = loop.run_until_complete(responses)

    consolidated_results = {}
    for item in results:
        consolidated_results.update(item)

    return consolidated_results

def save_data(data: dict):
    for ticker, items in data.items():
        stock_obj = Stocks.objects.get(ticker=ticker)
        ticker_obj, created = CurrentData.objects.get_or_create(stock=stock_obj)

        ticker_obj.change = items['change']
        ticker_obj.percent_change = items['percent_change']
        ticker_obj.open = items['open']
        ticker_obj.high = items['high']
        ticker_obj.low = items['low']
        ticker_obj.current = items['current']
        ticker_obj.previous = items['previous']
        ticker_obj.volume = items['volume']
        ticker_obj.value = items['value']
        ticker_obj.trades = items['trades']

        ticker_obj.save()