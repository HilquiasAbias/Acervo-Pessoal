from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(Item)
admin.site.register(Book)
admin.site.register(LendingBook)
admin.site.register(LendingItem)
