from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('Register',views.Register, name='Register'),
    path('',views.Register, name='Register')
]
