from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import PasswordChangeForm

form_class = PasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervo/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
