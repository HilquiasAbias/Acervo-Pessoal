from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('itens/', views.ItensView.as_view(), name='itens'),
]
