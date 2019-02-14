from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Passenger


class PassengerProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_view.html'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Passenger.objects.get(pk=self.request.user.id)
        return context
