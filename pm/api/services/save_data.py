import json
from api.models import Tickers, StockData

def save_tickers(tickers: list) -> None:
    """
    We save ticker data if it doesn't already exist
    """
    for ticker in tickers:
        data = Tickers.objects.filter(tickers=ticker)
        if data:
            pass
        else:
            tickers = Tickers(tickers=ticker)
            tickers.save()


def save_stock_data(dfs: dict) -> None:
    for i, ticker in enumerate(dfs['results']):
        ticker = next(iter(ticker))
        print("Starting: ",ticker)

        data = StockData.objects.filter(tickers=ticker)
        if data:
            print('data!')
            data.update(
                open=json.loads(f"{dfs['results'][i][ticker][0]['open']}"),
                high=json.loads(f"{dfs['results'][i][ticker][0]['high']}"),
                low=json.loads(f"{dfs['results'][i][ticker][0]['low']}"),
                close=json.loads(f"{dfs['results'][i][ticker][0]['close']}"),
                volume=json.loads(f"{dfs['results'][i][ticker][0]['volume']}"),
                value=json.loads(f"{dfs['results'][i][ticker][0]['value']}"),
                dates=json.loads(f"{dfs['results'][i][ticker][0]['date']}"),
            )
        else:
            ticker_guid = Tickers.objects.filter(tickers=ticker).first().GUID
            data = StockData(
                ticker_GUID = str(ticker_guid),
                tickers = str(ticker),
                open=json.loads(f"{dfs['results'][i][ticker][0]['open']}"),
                high = json.loads(f"{dfs['results'][i][ticker][0]['high']}"),
                low = json.loads(f"{dfs['results'][i][ticker][0]['low']}"),
                close = json.loads(f"{dfs['results'][i][ticker][0]['close']}"),
                volume = json.loads(f"{dfs['results'][i][ticker][0]['volume']}"),
                value = json.loads(f"{dfs['results'][i][ticker][0]['value']}"),
                dates = json.loads(f"{dfs['results'][i][ticker][0]['date']}"),
            )
            data.save()
