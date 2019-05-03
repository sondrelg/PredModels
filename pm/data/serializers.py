from rest_framework import serializers

class StockSerializer(serializers.Serializer):
    ticker = serializers.CharField()
    name = serializers.CharField()
    shares_outstanding = serializers.IntegerField()

class HistoricalDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    volume = serializers.IntegerField()

class CurrentDataSerializer(serializers.Serializer):
    stock = StockSerializer()
    change = serializers.FloatField()
    percent_change = serializers.FloatField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    current = serializers.FloatField()
    previous = serializers.FloatField()
    volume = serializers.IntegerField()
    value = serializers.IntegerField()
    trades = serializers.IntegerField()
    updated = serializers.DateTimeField()
    created = serializers.DateTimeField()