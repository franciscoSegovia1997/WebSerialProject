from django.urls import path, include
from . import views

app_name='appSerial'

urlpatterns = [
    path('',views.index,name='index')
]
