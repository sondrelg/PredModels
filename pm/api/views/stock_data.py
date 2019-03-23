from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import StockData

class ListHistory(APIView):
    """
    Returns list of Intility's customer companies.
    """
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

