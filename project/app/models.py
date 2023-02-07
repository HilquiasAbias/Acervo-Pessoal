from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    #cover_photo = models.ImageField(default=None)
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class LendingBook(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    #cover_photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class LendingItem(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
