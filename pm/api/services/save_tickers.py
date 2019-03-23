from api.services.get_history import get_stock_tickers

from .models import Tickers

def save_tickers(tickers: list):
    for ticker in tickers:
        db = Tickers(Tickers=ticker)
        db.save()
