from api.views.json import ViewRequest
from api.views.tickers import ListTickers
from api.views.stock_data import ListHistoryTSV
from api.views import api_docs
from api.views.daily_data import ListDaily
from django.urls import path, include

urlpatterns = [
    # Index
    path('', api_docs.api_docs, name='api_docs'),

    # Json paster
    path('json/', ViewRequest.as_view(), name='ViewRequest'),
    path('data/tickers/', ListTickers.as_view(), name='ViewRequest'),
   # path('data/<ticker>/', ListHistory.as_view(), name='ListHistory'),
    path('data/tsv/<ticker>/', ListHistoryTSV.as_view(), name='ListHistoryTSV'),
    path('data/daily/', ListDaily.as_view(), name='ListDaily'),
    ]