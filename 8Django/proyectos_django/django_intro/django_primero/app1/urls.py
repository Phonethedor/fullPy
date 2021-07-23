from django.urls import path
from .views import paginaInicio

urlpatterns = [
    path('', paginaInicio, name='inicio'),
]