

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incorrect_ticker/', views.wrong_ticker)
]
