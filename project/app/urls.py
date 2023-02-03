from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('', views.IndexView.as_view(), name='index'),
    path('entrar/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('trocar_senha/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='register'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('livros/', views.BooksView.as_view(), name='books'),
    path('itens/', views.ItensView.as_view(), name='itens'),
    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('emprestimos/', views.LendingsView.as_view(), name='lendings'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]

