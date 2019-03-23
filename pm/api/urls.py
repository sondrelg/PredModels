from api.views.json import ViewRequest

from django.urls import path, include

urlpatterns = [
    # Index
#    path('', include('docs.urls')),

    # Json paster
    path('json/', ViewRequest.as_view(), name='ViewRequest')

    path('tickers/', ViewRequest.as_view(), name='ViewRequest')
    ]