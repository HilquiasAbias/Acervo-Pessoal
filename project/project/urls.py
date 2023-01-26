from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import PasswordChangeForm

form_class = PasswordChangeForm

urlpatterns = [
    path('', RedirectView.as_view(url='acervo/')),
    path('admin/', admin.site.urls),
    path('acervo/', include('app.urls')),
]
