from django.urls import path

from core import views

urlpatterns = [
    path('', views.CountryTableView.as_view(), name='home'),
]
