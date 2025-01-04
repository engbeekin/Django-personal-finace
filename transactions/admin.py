from django.contrib import admin

from accounts.models import Account
from category.models import Category
from transactions.models import Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
