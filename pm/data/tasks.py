from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services.get_stocks import get_data as get_stock_data, save_stocks
from .services.get_current import get_data as get_current_data, save_data

@shared_task
def get_and_save_stock_data():
    data = get_stock_data()
    save_stocks(data)
    print('Successfully saved stocks')

@shared_task
def get_and_save_current_data():
    data = get_current_data()
    save_data(data)
    print('Successfully saved current data')