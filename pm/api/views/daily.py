from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from data.models import Stocks, CurrentData
from data.serializers import CurrentDataSerializer


class ListDaily(APIView):
    """
    Returns list of Intility's customer companies.
    """

    def get(self, request: Request):
        objects = CurrentData.objects.all()
        data = [CurrentDataSerializer(obj).data for obj in objects]

        adjusted_data = [{'ticker': i['stock']['ticker'],
                          'name': i['stock']['name'],
                          'change': i['change'],
                          'open': i['open'],
                          'high': i['high'],
                          'low': i['low'],
                          'current': i['current'],
                          'volume': i['volume'],
                          'value': i['value'],
                          'previous': i['previous'],
                          'trades': i['trades']}
                         for i in data]

        return Response(adjusted_data, 200)
