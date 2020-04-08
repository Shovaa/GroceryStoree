from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('Items',views.Items, name='items'),
    path('',views.Items, name='items')
]