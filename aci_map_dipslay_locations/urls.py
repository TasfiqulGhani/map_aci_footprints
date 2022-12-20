from django.urls import path

from . import views
from .apis import refreshApi

urlpatterns = [
    path('', views.loadpoints, name='displaylocation'),
    path('refresh/', refreshApi.as_view(), name='displaylocation'),
    path('loadpoints/', views.loadpoints, name='displaylocation'),
    path('getgeodata', views.geodata, name='displaylocation'),
    path('filter/', views.filter, name='displaylocation'),
    path('datadriven/', views.datadriven, name='displaylocation'),
]
