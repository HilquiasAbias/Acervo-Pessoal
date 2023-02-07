
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Contact, Item, Book, LendingBook, LendingItem
from django.contrib.auth.models import User

class TestView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        user = request.user
        action = 1
        itens = Item.objects.filter(user=user)
        books = Book.objects.filter(user=user)
        contacts = Contact.objects.filter(user=user)
        lendingItens = LendingItem.objects.filter(user=user)
        lendingBooks = LendingBook.objects.filter(user=user)

        return render(request, 'app/base_teste.html', {
            'user': user, 
            'action': action, 
            'itens': itens, 
            'books': books, 
            'contacts': contacts, 
            'lendings': {
                'on_itens': lendingItens,
                'on_books': lendingBooks
            }
        })
    
    def post(self, request):
        if self.action == 2: 
            pass # itens
        if self.action == 3:
            pass # books
        if self.action == 4:
            pass # contacts
        if self.action == 5:
            pass # lendings???
        pass

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class LoginView(TemplateView):
    template_name = 'app/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/acervo/dashboard')
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = self._authenticate_user(request, username, password)

        if user:
            login(request, user)
            return redirect('/acervo/dashboard')
        else:
            context = { 'error_message': 'Usuário ou senha incorretos!' }
            return render(request, self.template_name, context)

    def _authenticate_user(self, request, username, password):
        return authenticate(request, username=username, password=password)

class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/acervo/dashboard')
        else:
            return render(request, 'app/register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']

        if self._user_exists(email):
            context = {'error_message': 'Este usuário já existe.'}
        else:
            user = self._create_user(username, email, password)
            if user:
                self._create_user_models(user)
                return redirect('/acervo/login')

        return render(request, 'app/login.html', context)

    def _user_exists(self, email):
        return User.objects.filter(email=email).exists()

    def _create_user(self, username, email, password):
        try:
            user = User.objects.create_user(username=email, password=password, email=email)
            user.save()
            return user
        except:
            return None

    def _create_user_models(self, user):
        contacts = Contact.objects.create(user=user)
        contacts.save()
        itens = Item.objects.create(user=user)
        itens.save()
        books = Book.objects.create(user=user)
        books.save()

# class ChangePasswordView(LoginRequiredMixin, TemplateView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'app/password_change.html')

#     def post(self, request, *args, **kwargs):
#         pass

class DashboardView(LoginRequiredMixin, TemplateView): # 1
    def get(self, request, *args, **kwargs):
        user = request.user
        itens = Item.objects.filter(user=user)[:4]
        books = Book.objects.filter(user=user)[:4]
        contacts = Contact.objects.filter(user=user)[:4]
        lendingItens = LendingItem.objects.filter(user=user)[:4]
        lendingBooks = LendingBook.objects.filter(user=user)[:4]
        context = {
            "user": user,
            'itens': itens, 
            'books': books, 
            'contacts': contacts, 
            'lendings': {
                'on_itens': lendingItens,
                'on_books': lendingBooks
            }
        }
        return render(request, 'app/dashboard.html', context)

class BooksView(LoginRequiredMixin, TemplateView): # 3
    def get(self, request, *args, **kwargs):
        user = request.user
        books = Book.objects.filter(user=user)[:8]
        return render(request, 'app/books.html', {'user': user, 'books': books}) #

    def post(self, request, *args, **kwargs):
        pass

class ItensView(LoginRequiredMixin, TemplateView): # 2
    def get(self, request, *args, **kwargs):
        user = request.user
        itens = Item.objects.filter(user=user)[:8] # ALL, FILTER OU GET ???
        print(user)
        print(itens)
        return render(request, 'app/itens.html', {'user': user, 'itens': itens}) #

    def post(self, request, *args, **kwargs):
        pass

class ContactsView(LoginRequiredMixin, TemplateView): # 4
    def get(self, request, *args, **kwargs):
        user = request.user
        contacts = Contact.objects.filter(user=user)[:8]
        return render(request, 'app/contacts.html', {'user': user, 'contacts': contacts}) #

    def post(self, request, *args, **kwargs):
        pass

class LendingsView(LoginRequiredMixin, TemplateView): # 5
    def get(self, request, *args, **kwargs):
        user = request.user
        lendingItens = LendingItem.objects.filter(user=user)
        lendingBooks = LendingBook.objects.filter(user=user)
        context = {
            'user': user, 
            'lendingItens': lendingItens,
            'lendingBooks': lendingBooks
        }
        return render(request, 'app/lendings.html', context)

    def post(self, request, *args, **kwargs):
        pass

