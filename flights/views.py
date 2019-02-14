from django.views.generic import ListView, DetailView

from .models import Flight


class FlightsListView(ListView):
    template_name = 'flights_list.html'
    queryset = Flight.objects.all()
    context_object_name = 'flights'


class FlightDetailView(DetailView):
    template_name_suffix = ''
    template_name = 'flights_detail.html'
    model = Flight
    context_object_name = 'flight'
    slug_field = 'flight_code'
    slug_url_kwarg = 'flight_code'
