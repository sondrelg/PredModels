from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from api.services.get_history import get_stock_history

class ListHistory(APIView):
    """
    Returns list of Intility's customer companies.
    """
    def get(self, request: Request, ticker: str):
        try:
            #TODO: Replace this with DB get
            companies = get_stock_history(ticker)
        except Exception as e:
            print(e)
            return Response({'error': 'Failed querying database'}, status=500)
        return Response(companies, 200)

