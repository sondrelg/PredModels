from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from data.models import Stocks, HistoricalData
from data.serializers import HistoricalDataSerializer


class ListHistory(APIView):

    def get(self, request: Request, ticker: str):
        stock = Stocks.objects.get(ticker=ticker.upper())
        stock_data = HistoricalData.objects.filter(stock=stock)
        data = [HistoricalDataSerializer(i).data for i in stock_data]
        return Response(data)
