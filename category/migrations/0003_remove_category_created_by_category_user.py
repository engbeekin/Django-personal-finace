# Generated by Django 4.2.7 on 2025-01-04 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(db_column='created_by', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
