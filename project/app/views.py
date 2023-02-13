
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView
from .models import Contact, Item, Book, LendingBook, LendingItem
from django.contrib.auth.models import User

from django.db.models import Q
from django.utils import timezone

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

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/acervo')

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
                return redirect('/acervo/entrar')

        return render(request, 'app/login.html', context)

    def _user_exists(self, email):
        return User.objects.filter(email=email).exists()

    def _create_user(self, username, email, password):
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return user
        except:
            return None

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

# BOOKS

class BooksView(LoginRequiredMixin, TemplateView): # 3
    def get(self, request, *args, **kwargs):
        user = request.user
        books = Book.objects.filter(user=user).order_by('-created_at')

        return render(request, 'app/book/books.html', {'user': user, 'books': books})

class CreateBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/book/create_book.html', {'user': request.user})
    
    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        book = Book.objects.create(title=title, author=author, year=year, user=request.user)
        book.save()
        return redirect('/acervo/livros')

class DeleteBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        book.delete()
        return redirect('/acervo/livros')

class UpdateBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        book = Book.objects.get(pk=kwargs['pk'])
        return render(request, 'app/book/edit_book.html', { 'book': book, 'user': user })

    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']

        Book.objects.filter(pk=book.pk).update(
            title=title, 
            author=author, 
            year=year, 
            edited_at=timezone.now()
        )

        return redirect('/acervo/livros')

class SearchBookView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        search = request.POST.get('search')
        filters = request.POST.get('filters')
        
        if search:
            books = Book.objects.filter(user=user and Q(title__icontains=search))
        elif filters == None or filters == 1:
            books = Book.objects.filter(user=user).order_by('-edited_at')
        elif int(filters) == 2:
            books = Book.objects.filter(user=user).order_by('edited_at')
        else:
            return redirect('/acervo/livros')

        context = { 'books': books, 'user': user,  }
        return render(request, 'app/book/books.html', context)

# ITENS

class ItensView(LoginRequiredMixin, TemplateView): # 2
    def get(self, request, *args, **kwargs):
        user = request.user
        itens = Item.objects.filter(user=user).order_by('-created_at')[:6]
        return render(request, 'app/item/itens.html', {'user': user, 'itens': itens}) #

class CreateItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/item/create_item.html', {'user': request.user})
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        item = Item.objects.create(name=name, description=description, user=request.user)
        item.save()
        return redirect('/acervo/itens')

class DeleteItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['pk'])
        item.delete()
        return redirect('/acervo/itens')

class UpdateItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        item = Item.objects.get(pk=kwargs['pk'])
        return render(request, 'app/item/edit_item.html', { 'item': item, 'user': user })

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['pk'])
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']

        Item.objects.filter(pk=item.pk).update(
            title=title, 
            author=author, 
            year=year, 
            edited_at=timezone.now()
        )

        return redirect('/acervo/itens')

class SearchItemView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        search = request.POST.get('search')
        filters = request.POST.get('filters')
        
        if search:
            itens = Item.objects.filter(user=user and Q(title__icontains=search))
        elif filters == None or filters == 1:
            itens = Item.objects.filter(user=user).order_by('-edited_at')
        elif int(filters) == 2:
            itens = Item.objects.filter(user=user).order_by('edited_at')
        else:
            return redirect('/acervo/livros')

        context = { 'itens': itens, 'user': user,  }
        return render(request, 'app/item/itens.html', context)

# CONTACTS

class ContactsView(LoginRequiredMixin, TemplateView): # 4
    def get(self, request, *args, **kwargs):
        user = request.user
        contacts = Contact.objects.filter(user=user).order_by('-created_at')[:6]
        return render(request, 'app/contact/contacts.html', {'user': user, 'contacts': contacts}) #

class CreateContactView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact/create_contact.html', {'user': request.user})
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        contact = Contact.objects.create(name=name, email=email, user=request.user)
        contact.save()
        return redirect('/acervo/contatos')

class DeleteContactView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        contact = Contact.objects.get(pk=kwargs['pk'])
        contact.delete()
        return redirect('/acervo/contatos')

class UpdateContactView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        contact = Contact.objects.get(pk=kwargs['pk'])
        return render(request, 'app/contact/edit_contact.html', { 'contact': contact, 'user': user })

    def post(self, request, *args, **kwargs):
        contact = Contact.objects.get(pk=kwargs['pk'])
        name = request.POST['name']
        email = request.POST['email']

        Contact.objects.filter(pk=contact.pk).update(
            name=name, 
            email=email,
            edited_at=timezone.now()
        )

        return redirect('/acervo/contatos')

class SearchContactView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        search = request.POST.get('search')
        filters = request.POST.get('filters')
        
        if search:
            contacts = Contact.objects.filter(user=user and Q(title__icontains=search))
        elif filters == None or filters == 1:
            contacts = Contact.objects.filter(user=user).order_by('-edited_at')
        elif int(filters) == 2:
            contacts = Contact.objects.filter(user=user).order_by('edited_at')
        else:
            return redirect('/acervo/contatos')

        context = { 'contacts': contacts, 'user': user  }
        return render(request, 'app/contact/contacts.html', context)



# LENDINGS

class LendingsView(LoginRequiredMixin, TemplateView): # 5
    def get(self, request, *args, **kwargs):
        user = request.user
        lendingItens = LendingItem.objects.filter(user=user).order_by('-edited_at')
        lendingBooks = LendingBook.objects.filter(user=user).order_by('-edited_at')
        context = {
            'user': user, 
            'lendingItens': lendingItens,
            'lendingBooks': lendingBooks
        }
        return render(request, 'app/lendings/lendings.html', context)


class SearchLendingView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        search_type = request.POST.get('search-type')
        lendingItens = LendingItem.objects.filter(user=user).order_by('-edited_at')
        lendingBooks = LendingBook.objects.filter(user=user).order_by('-edited_at')
        lendings = None

        if search_type == 'item':
            search_item = request.POST.get('search-item')
            filters_item = request.POST.get('filters-item')

            if search_item:
                lendings = LendingBook.objects.filter(user=user and Q(title__icontains=search_item))
            elif filters_item == None or filters_item == 1:
                lendings = LendingBook.objects.filter(user=user).order_by('-edited_at')
            elif int(filters_item) == 2:
                lendings = LendingBook.objects.filter(user=user).order_by('edited_at')
            elif int(filters_item) == 3:
                lendings = LendingBook.objects.filter(user=user, on_lending=False).order_by('-edited_at')
            elif int(filters_item) == 4:
                lendings = LendingBook.objects.filter(user=user, on_lending=True).order_by('-edited_at')
            else:
                return redirect('/acervo/emprestimos')

            context = { 'lendingItens': lendings, 'lendingBooks': lendingBooks, 'user': user  }
            return render(request, 'app/lendings/lendings.html', context)

        else:
            search_book = request.POST.get('search-book')
            filters_book = request.POST.get('filters-book')

            if search_book:
                lendings = LendingBook.objects.filter(user=user and Q(title__icontains=search_book))
            elif filters_book == None or filters_book == 1:
                lendings = LendingBook.objects.filter(user=user).order_by('-edited_at')
            elif int(filters_book) == 2:
                lendings = LendingBook.objects.filter(user=user).order_by('edited_at')
            elif int(filters_book) == 3:
                lendings = LendingBook.objects.filter(user=user, on_lending=False).order_by('-edited_at')
            elif int(filters_book) == 4:
                lendings = LendingBook.objects.filter(user=user, on_lending=True).order_by('-edited_at')
            else:
                return redirect('/acervo/emprestimos')

            context = { 'lendingItens': lendingItens, 'lendingBooks': lendings, 'user': user  }
            return render(request, 'app/lendings/lendings.html', context)

# LENDING ITEM

class CreateLendingItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        contacts = Contact.objects.filter(user=user).order_by('-created_at')
        itens = Item.objects.filter(user=user).order_by('-created_at')
        context = {
            'user': user,
            'itens': itens,
            'contacts': contacts,
        }
        return render(request, 'app/lendings/item/create_lending_item.html', context)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        contact = Contact.objects.get(pk=request.POST['contact'])

        item = Item.objects.get(pk=request.POST['item'])
        item.on_lending = True
        item.save()

        lending_item = LendingItem.objects.create(
            user=user,
            contact=contact,
            item=item
        )
        lending_item.save()
        
        return redirect('/acervo/emprestimos')

class DeleteLendingItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        lending_item = LendingItem.objects.get(pk=kwargs['pk'])
        lending_item.delete()
        return redirect('/acervo/emprestimos')

class UpdateLendingItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        lending_item = LendingItem.objects.get(pk=kwargs['pk'])
        contacts = Contact.objects.filter(user=user).order_by('-created_at')
        itens = Item.objects.filter(user=user).order_by('-created_at')
        current_item = lending_item.item
        current_contact = lending_item.contact

        context = {
            'user':user,
            'lending_item':lending_item,
            'itens':itens,
            'contacts':contacts,
            'current_item':current_item,
            'current_contact':current_contact,
        }
            
        return render(request, 'app/lendings/item/edit_lending_item.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        contact = Contact.objects.get(pk=request.POST['contact'])
        item = Item.objects.get(pk=request.POST['item'])

        lending_item = LendingItem.objects.get(pk=kwargs['pk'])
        lending_item.user = user
        lending_item.contact = contact
        lending_item.item = item
        lending_item.edited_at = timezone.now()
        lending_item.save()

        return redirect('/acervo/emprestimos')

class EndLendingItemView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        lending_item = LendingItem.objects.get(pk=kwargs['pk'])
        lending_item.on_lending = False
        lending_item.save()
        item = lending_item.item
        item.on_lending = False
        item.save()
        return redirect('/acervo/emprestimos')


# LENDING BOOK

class CreateLendingBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        contacts = Contact.objects.filter(user=user).order_by('-created_at')
        books = Book.objects.filter(user=user).order_by('-created_at')
        context = {
            'user': user,
            'books': books,
            'contacts': contacts,
        }
        return render(request, 'app/lendings/book/create_lending_book.html', context)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        contact = Contact.objects.get(pk=request.POST['contact'])

        book = Book.objects.get(pk=request.POST['book'])
        book.on_lending = True
        book.save()

        lending_book = LendingBook.objects.create(
            user=user,
            contact=contact,
            book=book
        )
        lending_book.save()
        
        return redirect('/acervo/emprestimos')

class DeleteLendingBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        lending_book = LendingBook.objects.get(pk=kwargs['pk'])
        lending_book.delete()
        return redirect('/acervo/emprestimos')

class UpdateLendingBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        lending_book = LendingBook.objects.get(pk=kwargs['pk'])
        contacts = Contact.objects.filter(user=user).order_by('-created_at')
        books = Book.objects.filter(user=user).order_by('-created_at')
        current_book = lending_book.book
        current_contact = lending_book.contact

        context = {
            'user':user,
            'lending_book':lending_book,
            'books':books,
            'contacts':contacts,
            'current_book':current_book,
            'current_contact':current_contact,
        }
            
        return render(request, 'app/lendings/book/edit_lending_book.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        contact = Contact.objects.get(pk=request.POST['contact'])
        book = Book.objects.get(pk=request.POST['book'])

        lending_book = LendingBook.objects.get(pk=kwargs['pk'])
        lending_book.user = user
        lending_book.contact = contact
        lending_book.book = book
        lending_book.edited_at = timezone.now()
        lending_book.save()

        return redirect('/acervo/emprestimos')

class EndLendingBookView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        lending_book = LendingBook.objects.get(pk=kwargs['pk'])
        lending_book.on_lending = False
        lending_book.save()
        book = lending_book.book
        book.on_lending = False
        book.save()
        return redirect('/acervo/emprestimos')


# class SearchLendingBookView(LoginRequiredMixin, TemplateView):
#     def post(self, request, *args, **kwargs):
#         user = request.user
#         search = request.POST.get('search')
#         filters = request.POST.get('filters')
        
#         if search:
#             lendings = LendingBook.objects.filter(user=user and Q(title__icontains=search))
#         elif filters == None or filters == 1:
#             lendings = LendingBook.objects.filter(user=user).order_by('-edited_at')
#         elif int(filters) == 2:
#             lendings = LendingBook.objects.filter(user=user).order_by('edited_at')
#         elif int(filters) == 3:
#             lendings = LendingBook.objects.filter(user=user, on_lending=False).order_by('-edited_at')
#         elif int(filters) == 4:
#             lendings = LendingBook.objects.filter(user=user, on_lending=True).order_by('-edited_at')
#         else:
#             return redirect('/acervo/emprestimos')

#         context = { 'lendingItens': lendings, 'user': user  }
#         return render(request, 'app/lendings/lendings.html', context)

# class SearchLendingItemView(LoginRequiredMixin, TemplateView):
#     def post(self, request, *args, **kwargs):
#         user = request.user
#         search = request.POST.get('search')
#         filters = request.POST.get('filters')
        
#         if search:
#             lendings = LendingItem.objects.filter(user=user and Q(title__icontains=search))
#         elif filters == None or filters == 1:
#             lendings = LendingItem.objects.filter(user=user).order_by('-edited_at')
#         elif int(filters) == 2:
#             lendings = LendingItem.objects.filter(user=user).order_by('edited_at')
#         elif int(filters) == 3:
#             lendings = LendingItem.objects.filter(user=user, on_lending=False).order_by('-edited_at')
#         elif int(filters) == 4:
#             lendings = LendingItem.objects.filter(user=user, on_lending=True).order_by('-edited_at')
#         else:
#             return redirect('/acervo/emprestimos')

#         context = { 'lendingItens': lendings, 'user': user  }
#         return render(request, 'app/lendings/lendings.html', context)
