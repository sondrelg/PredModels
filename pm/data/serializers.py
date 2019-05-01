from rest_framework import serializers

class StockSerializer(serializers.Serializer):
    ticker = serializers.CharField()
    name = serializers.CharField()
    shares_outstanding = serializers.IntegerField()

from django.core import serializers
objectQuerySet = Stocks.objects.ticker()
data = serializers.serialize('json', objectQuerySet, fields=('fileName','id'))