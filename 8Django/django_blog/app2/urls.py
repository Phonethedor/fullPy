from django.urls import path
from .views import index,inicio, info

urlpatterns = [
    path('aplicacion/', index),
    path('inicio/', inicio.as_view, name='inicio'),
    path('info/', info.as_view, name='info'),
]