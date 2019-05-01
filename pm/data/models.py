from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.
class Stocks(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    ticker = models.CharField(max_length=15, null=False, blank=False, unique=True)
    name = models.CharField(max_length=250, null=False, blank=False, unique=False)
    shares_outstanding = models.IntegerField(null=True)


class CurrentData(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, blank=False, null=False, primary_key=True)
    change = models.FloatField(null=True, blank=False)
    percent_change = models.FloatField(null=True, blank=False)
    open = models.FloatField(null=True, blank=False)
    high = models.FloatField(null=True, blank=False)
    low = models.FloatField(null=True, blank=False)
    current = models.FloatField(null=True, blank=False)
    previous = models.FloatField(null=True, blank=False)
    volume = models.IntegerField(null=True, blank=False)
    value = models.IntegerField(null=True, blank=False)
    trades = models.IntegerField(null=True, blank=False)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CurrentData, self).save(*args, **kwargs)

class HistoricalData(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4(), editable=False, blank=True)
    date = models.DateField()
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, blank=False, null=False, unique=False)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
