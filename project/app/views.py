from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin  # para classes. EX: class MyClass(LoginRequiredMixin, TemplateView)

def index(request):
    return render(request, 'app/index.html')


@login_required
def page_one(request):
    return render(request, 'app/page_one.html', { 'name': request.user.username })
