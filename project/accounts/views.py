from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User

class register(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/register.html')

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
        return HttpResponseRedirect(reverse('app:index'))
