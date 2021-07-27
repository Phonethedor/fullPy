from django.urls import path
from . import views
from .views import inicio, info

urlpatterns = [
    path('aplicacion/', views.index),
    path('inicio/', inicio.as_view, name='inicio'),
    path('info/', info.as_view, name='info'),
]