from django.db import models
from uuid import uuid4

# Create your models here.
class Tickers(models.Model):
    GUID = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    tickers = models.CharField(max_length=30)

    class Meta:
        ordering = ('tickers',)

class StockData(models.Model):
    ticker_GUID = models.CharField(max_length=100, blank=False)
    GUID = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)
    tickers = models.CharField(max_length=30, default="Placeholder")
    open = models.TextField() 
    high = models.TextField() 
    low = models.TextField() 
    close = models.TextField() 
    volume = models.TextField() 
    value = models.TextField()
    dates = models.TextField()

    class Meta:
        ordering = ('tickers',)