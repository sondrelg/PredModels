from datetime import datetime
from aioify import aioify
import urllib.request
import asyncio
import csv


from ..models import Stocks, HistoricalData


def get_stock_history(ticker: str):
    print(ticker)
    url = f"https://www.netfonds.no/quotes/paperhistory.php?paper={ticker}.OSE&csv_format=csv"
    response = urllib.request.urlopen(url)

    raw_data = response.read().decode('ISO-8859-1')
    row_data = raw_data.strip().split('\n')[1:]

    reader = csv.reader(row_data, delimiter=',')
    for row in reader:

        raw_date = row[0]
        loaded_date = datetime.strptime(raw_date, '%Y%m%d')
        adjusted_date = loaded_date.strftime('%Y-%m-%d')

        try:
            stock = Stocks.objects.get(ticker=ticker)
            obj, created = HistoricalData.objects.get_or_create(stock=stock, date=adjusted_date)

            # TODO: Remove when everythign is added
            if not created:
                break

            obj.open = row[3]
            obj.high = row[4]
            obj.low = row[5]
            obj.close = row[6]
            obj.volume = row[7]
            obj.value = row[8]
            obj.save()
        except Exception as e:
            print(f'Failed saving {ticker}: {e}')

def get_stock_histories() -> dict:
    tickers = [ticker['ticker'] for ticker in Stocks.objects.values('ticker')]
    for ticker in tickers:
        get_stock_history(ticker)
