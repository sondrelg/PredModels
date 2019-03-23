from django.db import models

# Create your models here.
class Tickers(models.Model):
    GUID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    Ticker = models.CharField(max_length=30)