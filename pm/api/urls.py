from .views import api_docs
from .views.historical import ListHistory
from .views.daily import ListDaily

from .views.json import ViewRequest
from .views.tickers import ListTickers

from django.urls import path, include

urlpatterns = [
    # Index
    path('', api_docs.api_docs, name='api_docs'),

    path('json/', ViewRequest.as_view(), name='ViewRequest'),
    path('data/tickers/', ListTickers.as_view(), name='ViewRequest'),
    path('data/daily/', ListDaily.as_view(), name='ListDaily'),
    path('data/ticker/<ticker>/', ListHistory.as_view(), name='ListHistory'),

]
