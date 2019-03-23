from api.views.json import ViewRequest
from api.views.tickers import ListTickers



from django.urls import path, include

urlpatterns = [
    # Index
#    path('', include('docs.urls')),

    # Json paster
    path('json/', ViewRequest.as_view(), name='ViewRequest'),

    path('tickers/', ListTickers.as_view(), name='ViewRequest'),
    ]