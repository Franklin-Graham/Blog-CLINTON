from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun1, name='fun1'),
    path('message',views.message,name='message')
]
