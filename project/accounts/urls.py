from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logout'), name='logout'),
    path(
        'password_change/', 
        auth_views.PasswordChangeView.as_view( template_name='registration/password_change.html' ), 
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view( template_name='registration/password_change_done.html' ),
        name='password_change_done',
    ),
]
