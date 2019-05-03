from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from data.models import Stocks

class ListTickers(APIView):
    """
    Returns list of Intility's customer companies.
    """
    def get(self, request: Request):
        try:
            tickers = [i[0] for i in Stocks.objects.values_list('ticker')]
        except Exception as e:
            print(e)
            return Response({'error': 'Failed querying database'}, status=500)
        return Response(tickers, 200)

