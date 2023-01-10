from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path(
        'password_change/', auth_views.PasswordChangeView.as_view( template_name='registration/password_change.html' ), name="password_change"
        ),
]