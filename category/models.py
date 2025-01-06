from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=CASCADE, db_column="created_by")
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f" {self.name}"