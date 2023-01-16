from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # para classes. EX: class MyClass(LoginRequiredMixin, TemplateView)
from django.views.generic import TemplateView
from . import models #Profile, Contact, Item, Book, LendingBook, LendingItem

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')


class ItensView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.filter(user=user)
        itens = Item.objects.filter(profile=profile)
        return render(request, 'app/itens.html', {'user': user, 'profile': profile, 'itens': itens})

    def post(self, request, *args, **kwargs):


        return HttpResponseRedirect(reverse('app:index'))

@login_required
def page_one(request):
    return render(request, 'app/page_one.html', { 'name': request.user.username })

