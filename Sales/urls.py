from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.Sales, name='Sales'),
    path('ContractBuyer',views.ContractBuyer, name='ContractBuyer')
]
