from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

import passengers.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', include(passengers.urls)),
]
