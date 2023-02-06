from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('', views.IndexView.as_view(), name='index'),
    path('entrar/', views.LoginView.as_view(), name='login'),
    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('trocar_senha/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='password_change'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('livros/', views.BooksView.as_view(), name='books'),
    path('itens/', views.ItensView.as_view(), name='itens'),
    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('emprestimos/', views.LendingsView.as_view(), name='lendings'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]

