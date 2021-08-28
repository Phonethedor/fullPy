from django.urls import path
from . import views     

urlpatterns = [
    path('', views.index),
    path('azar', views.index),
    path('reinicio', views.reinicio),
]