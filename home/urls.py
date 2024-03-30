from django.contrib import admin
from django.urls import path
from . import views

# URL patterns for the 'home' app
urlpatterns = [
    path('', views.index, name='home')
]

"""
URL patterns for homr views.
"""
