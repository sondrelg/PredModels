from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services.get_stocks import get_data as get_stock_data
from .services.save_stocks import save_stocks

@shared_task
def get_and_save_stock_data:
    data = get_stock_data()
    save_stocks(data)
    print('Successfully saved stocks')