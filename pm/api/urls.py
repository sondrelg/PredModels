from api.views.json import ViewRequest
from api.views.tickers import ListTickers
from api.views.history import ListHistory


from django.urls import path, include

urlpatterns = [
    # Index
#    path('', include('docs.urls')),

    # Json paster
    path('json/', ViewRequest.as_view(), name='ViewRequest'),
    path('data/tickers', ListTickers.as_view(), name='ViewRequest'),
    path('data/<ticker>', ListHistory.as_view(), name='ListHistory')
    ]