from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from accounts.models import Account
from category.models import Category


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        EXPENSE = 'expense'
        INCOME = 'income'

    account = models.ForeignKey(Account, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    type_of_transaction = models.CharField(max_length=10, choices=TransactionType.choices)
    Amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=CASCADE, db_column="created_by", null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.account} ({self.type_of_transaction})"
