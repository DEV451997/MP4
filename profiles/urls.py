from django.urls import path
from . import views
# Urls for profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
]


"""
URL patterns for profile views.
"""
