from django.views.generic import ListView

from .models import Flight


class FlightsListView(ListView):
    template_name = 'flights_list.html'
    queryset = Flight.objects.all()
    context_object_name = 'flights'
