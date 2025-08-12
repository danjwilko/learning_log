""" Defines URL patterns for accounts."""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include the default auth URLs.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
