from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'transactions'),
    path('income_transactions/',views.income_transactions , name = 'income_transactions'),
    path('expense_transactions/',views.expense_transactions, name = 'expense_transactions'),
    path('create/',views.create, name = 'create'),
    path('update/<int:transaction_id>',views.update, name = 'update-transaction'),
    path('delete/<int:transaction_id>',views.delete, name = 'delete-transaction'),
]