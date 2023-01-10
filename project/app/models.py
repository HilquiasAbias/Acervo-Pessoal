from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    cover_photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LendingBook(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    cover_photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LendingItem(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
