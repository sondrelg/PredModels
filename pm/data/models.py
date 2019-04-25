from django.db import models
from uuid import uuid4


# Create your models here.
class Stocks(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    ticker = models.CharField(max_length=15, null=False, blank=False, unique=True)
    name = models.CharField(max_length=250, null=False, blank=False, unique=False)
    shares_outstanding = models.IntegerField(null=True)


class CurrentData(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4(), editable=False, blank=True)
    stock = models.OneToOneField(Stocks, on_delete=models.CASCADE, blank=False, null=False)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)


class HistoricalData(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4(), editable=False, blank=True)
    date = models.DateField()
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, blank=False, null=False, unique=False)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
