from django.urls import path, include

from .views import FlightsListView

app_name = 'flights'

urlpatterns = [
    path('flights/', FlightsListView.as_view(), name='flights-list')
]
