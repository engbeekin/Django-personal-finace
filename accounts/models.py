from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Account(models.Model):
    name = models.CharField(max_length=64)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=CASCADE, db_column="created_by")
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return f" {self.name}"