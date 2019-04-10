from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r

#from api.models import StockData
from api.services.get_data import get_stock_history_tsv
"""
class ListHistory(APIView):
    def get(self, request: Request, ticker: str):
        try:
            stock_data = StockData.objects.get(tickers=ticker.upper())
            stock_data = {ticker.upper():{'open':stock_data.open,
                          'close':stock_data.close,
                          'high':stock_data.high,
                          'low':stock_data.low,
                          'value':stock_data.value,
                          'volume':stock_data.volume,
                          'date':stock_data.dates}}
        except Exception as e:
            print(e)
            return Response({'error': 'Failed querying database'}, status=500)
        return Response(stock_data, 200)
"""
class ListHistoryTSV(APIView):
    """
    Returns list of Intility's customer companies.
    """

    def get(self, request: Request, ticker: str):
        try:
            stock_data = get_stock_history_tsv(ticker)
        except Exception as e:
            print(e)
            return Response({'error': 'Failed querying database'}, status=500)
        return Response(stock_data)

