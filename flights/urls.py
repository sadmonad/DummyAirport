from django.urls import path, include

from .views import FlightsListView, FlightDetailView

app_name = 'flights'

urlpatterns = [
    path('flights/', FlightsListView.as_view(), name='list'),
    path('flights/<slug:flight_code>/', FlightDetailView.as_view(), name='detail')
]
