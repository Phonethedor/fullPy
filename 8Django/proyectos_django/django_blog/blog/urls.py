from django.urls import path
from .views import *

urlpatterns = [
    path('', root, name='inicio'),
    path('blogs', index),
    path('blogs/new', new),
    path('blogs/create', create),
    path('blogs/<int:numero>', create),
    path('blogs/<int:numero>/edit', edit),
    path('blogs/<int:numero>/delete', edit),
    path('blogs/json', json),
]
