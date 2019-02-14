from django.urls import path, include

from .views import PassengerProfileView


urlpatterns = [
    path('accounts/profile/', PassengerProfileView.as_view(), name='profile')
]
