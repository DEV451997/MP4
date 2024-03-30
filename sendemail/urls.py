from django.urls import path
from .views import ContactView

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
]

"""
URL pattern for the contact page.
"""
