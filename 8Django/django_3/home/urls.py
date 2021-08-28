from django.urls import path
from . import views

urlpatterns = [
    path('', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista2/', views.ListarPrueba.as_view()),
    path('create/', views.CreateViewPrueba.as_view()),
]