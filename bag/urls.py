from django.urls import path
from . import views

# List of URL patterns for the 'bag' app
urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]

"""
URL patterns for the 'bag' app.

This list of URL patterns maps specific URL paths to corresponding view functions
defined in the 'views.py' module of the 'bag' app. Each path consists of a unique
identifier and specifies the view function that should be invoked when the URL is
accessed. The 'name' attribute is used to uniquely identify each URL pattern and
can be referred to in Django templates or views to generate URLs dynamically.
"""
