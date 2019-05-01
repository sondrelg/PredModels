from rest_framework import serializers

class StockSerializer(serializers.Serializer):
    ticker = serializers.CharField()
    name = serializers.CharField()
    shares_outstanding = serializers.IntegerField()

