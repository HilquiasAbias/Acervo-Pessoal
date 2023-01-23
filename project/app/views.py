from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Contact, Item, Book, LendingBook, LendingItem
from django.contrib.auth.models import User

class TestView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        user = request.user
        action = 1
        return render(request, 'app/base_teste.html', {'user': user, 'action': action})
    
    def post(self, request):
        pass

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class DashboardView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'app/dashboard.html', {'user': user})

class ItensView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        itens = Item.objects.filter(user=user)[1]
        print(user)
        print(itens)
        return render(request, 'app/itens.html', {'user': user, 'itens': itens}) #

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('acervo:index'))

class BooksView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        books = Book.objects.filter(user=user)[1]
        return render(request, 'app/books.html', {'user': user, 'books': books}) #

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('acervo:index'))

class LendingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        #lendings = Lendings.objects.get(user=user)
        return render(request, 'app/lendings.html', {'user': user}) #, 'lendings': lendings

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('acervo:index'))

class ContactsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        contacts = Contact.objects.filter(user=user)[1]
        return render(request, 'app/contacts.html', {'user': user, 'contacts': contacts}) #

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('acervo:index'))

class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']

        userExists = User.objects.filter(email=email).first()
        if userExists:
            pass

        user = User.objects.create_user(username=username, email=email, password=password)

        contacts = Contact.objects.create(user=user)
        itens = Item.objects.create(user=user)
        books = Book.objects.create(user=user)
        # lendingsItens = LendingItem.objects.create(user=user)
        # lendingsBooks = LendingBook.objects.create(user=user)

        contacts.save()
        itens.save()
        books.save()
        # lendingsItens.save()
        # lendingsBooks.save()
        user.save()

        return render(request, 'app/login.html')
