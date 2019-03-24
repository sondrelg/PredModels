from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.models, name='models'),
    path('treemap/', views.treemap, name='treemap'),
]
