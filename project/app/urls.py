from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('', views.IndexView.as_view(), name='index'),

    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('entrar/', views.LoginView.as_view(), name='login'),
    path('trocar_senha/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='password_change'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('livros/', views.BooksView.as_view(), name='books'),
    path('livros/<int:pk>/apagando', views.DeleteBookView.as_view(), name='delete_book'),

    path('itens/', views.ItensView.as_view(), name='itens'),
    path('itens/<int:pk>/apagando', views.DeleteItemView.as_view(), name='delete_item'),

    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('contatos/<int:pk>/apagando', views.DeleteContactView.as_view(), name='delete_contact'),

    path('emprestimos/', views.LendingsView.as_view(), name='lendings'),
]
