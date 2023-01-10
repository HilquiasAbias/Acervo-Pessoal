from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views #as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervo/', include('app.urls'), name='acervo'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('accounts/', include('views.urls'), name='accounts') 
]
