from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('emprestimos/', views.LendingsView.as_view(), name='lendings'),
    path('itens/', views.ItensView.as_view(), name='itens'),
    path('livros/', views.BooksView.as_view(), name='books'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]

