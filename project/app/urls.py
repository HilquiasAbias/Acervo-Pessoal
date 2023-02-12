from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('cadastro/', views.RegisterView.as_view(), name='register'),
    path('entrar/', views.LoginView.as_view(), name='login'),
    path('trocar_senha/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='password_change'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('livros/', views.BooksView.as_view(), name='books'),
    path('livros/criar', views.CreateBookView.as_view(), name='create_book'),
    path('livros/buscar', views.SearchBookView.as_view(), name='search_book'),
    path('livros/<int:pk>/apagar', views.DeleteBookView.as_view(), name='delete_book'),
    path('livros/<int:pk>/editar', views.UpdateBookView.as_view(), name='update_book'),

    path('itens/', views.ItensView.as_view(), name='itens'),
    path('itens/criar', views.CreateItemView.as_view(), name='create_item'),
    path('itens/buscar', views.SearchItemView.as_view(), name='search_item'),
    path('itens/<int:pk>/apagar', views.DeleteItemView.as_view(), name='delete_item'),
    path('itens/<int:pk>/editar', views.UpdateItemView.as_view(), name='update_item'),

    path('contatos/', views.ContactsView.as_view(), name='contacts'),
    path('contatos/criar', views.CreateContactView.as_view(), name='create_contact'),
    path('contatos/buscar', views.SearchContactView.as_view(), name='search_contact'),
    path('contatos/<int:pk>/apagar', views.DeleteContactView.as_view(), name='delete_contact'),
    path('contatos/<int:pk>/editar', views.UpdateContactView.as_view(), name='update_contact'),
    
    path('emprestimos/', views.LendingsView.as_view(), name='lendings'),
    path('emprestimos/buscar', views.SearchLendingView.as_view(), name='search_lending'),

    path('emprestimos/item/criar', views.CreateLendingItemView.as_view(), name='create_lending_item'),
    path('emprestimos/item/<int:pk>/finalizar', views.EndLendingItemView.as_view(), name='end_lending_item'),
    path('emprestimos/item/<int:pk>/editar', views.UpdateLendingItemView.as_view(), name='update_lending_item'),
    path('emprestimos/item/<int:pk>/apagar', views.DeleteLendingItemView.as_view(), name='delete_lending_item'),

    path('emprestimos/livro/criar', views.CreateLendingBookView.as_view(), name='create_lending_book'),
    path('emprestimos/livro/<int:pk>/finalizar', views.EndLendingBookView.as_view(), name='end_lending_book'),
    path('emprestimos/livro/<int:pk>/editar', views.UpdateLendingBookView.as_view(), name='update_lending_book'),
    path('emprestimos/livro/<int:pk>/apagar', views.DeleteLendingBookView.as_view(), name='delete_lending_book'),
]
