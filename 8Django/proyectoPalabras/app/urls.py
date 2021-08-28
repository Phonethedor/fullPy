from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generar', views.generar),
    url(r'^limpiar', views.limpiar),
]