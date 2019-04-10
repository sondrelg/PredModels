from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from api.services.get_data import mock_endpoint

class ListDaily(APIView):
    """
    Returns list of Intility's customer companies.
    """
    def get(self, request: Request):
        data = mock_endpoint()
        return Response(data, 200)
