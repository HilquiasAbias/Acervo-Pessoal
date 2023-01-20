from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Profile, Contact, Item, Book, LendingBook, LendingItem

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
        profile = Profile.objects.filter(user=user).first()
        #itens = Item.objects.get(profile=profile)
        return render(request, 'app/itens.html', {'user': user, 'profile': profile}) #, 'itens': itens

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('acervo:index'))

class BooksView(LoginRequiredMixin, TemplateView):
    pass

class LendingsView(LoginRequiredMixin, TemplateView):
    pass

class ContactsView(LoginRequiredMixin, TemplateView):
    pass

class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']

        userExists = User.objects.filter(email=email).first()
        if userExists:
            return HttpResponse('Já existe com esse email.')

        user = User.objects.create_user(username=username, email=email, password=password)
        print(user)
        user.save()
        return HttpResponseRedirect('app/login.html')
