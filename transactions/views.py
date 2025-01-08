from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from accounts.models import Account
from .form import TransactionForm
from .models import Transaction


@login_required
def index(request):
    transactions = Transaction.objects.select_related('user', 'account', 'category').order_by('-id')

    return render(request, 'index.html', {'transactions': transactions})


@login_required
def income_transactions(request):
    transactions = (Transaction.objects.filter(type_of_transaction='income')
                    .select_related('user', 'account', 'category').order_by('-id'))

    return render(request, 'income-list.html', {'transactions': transactions})


@login_required
def expense_transactions(request: object) -> object:
    transactions = (Transaction.objects.filter(type_of_transaction='expense')
                    .select_related('user', 'account', 'category').all())

    return render(request, 'expense-list.html', {'transactions': transactions})


@login_required
@transaction.atomic
def create(request) -> object:
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            try:
                process_transaction(request, form)
                messages.success(request, 'Transaction created successfully!')
                return redirect('transactions')
            except Exception as e:
                print(f"Error: {e}")
                return render(request, 'create.html',
                              {'form': form, 'error': e})

    form = TransactionForm()
    return render(request, 'create.html', {'form': form})


@login_required
@transaction.atomic
def update(request, transaction_id: int):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    form = TransactionForm(request.POST or None, instance=transaction)
    old_transaction_amount = transaction.Amount
    print(f'transaction db amount: {transaction.Amount}')
    print(f'transaction request amount: {old_transaction_amount}')
    if form.is_valid():
        try:
            process_transaction(request, form, old_transaction_amount)
            messages.success(request, 'Transaction Updated successfully!')
            return redirect('transactions')
        except Exception as e:
            return render(request, 'edit.html',
                          {'form': form, 'transaction': transaction, 'error': e})

    return render(request, 'edit.html', {'form': form, 'transaction': transaction})


@login_required
@transaction.atomic
def delete(request, transaction_id: int):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    transaction.delete()
    update_account_balance_after_delete_transaction(transaction.account_id, transaction.Amount)
    messages.success(request, 'Deleted Transaction successfully!')
    return redirect('/')


def process_transaction(request, form, old_transaction_amount=0):
    account_id = form.cleaned_data['account'].id
    transaction_type = form.cleaned_data['type_of_transaction']

    # updated the account balance after transaction is updated
    transaction_amount = abs(Decimal(old_transaction_amount) - form.cleaned_data['Amount'])
    account = Account.objects.get(pk=account_id)

    # validate the transaction amount if exceed the account balance
    check_if_account_balance_exceed(account.balance, transaction_amount, transaction_type)
    transaction = form.save(commit=False)
    transaction.user = request.user
    transaction.save()

    # update the account balance after transaction
    update_account_balance(account, transaction_amount, transaction_type)


def update_account_balance(account, transaction_amount, transaction_type):
    if transaction_type == Transaction.TransactionType.INCOME:
        account.balance += transaction_amount
    elif transaction_type == Transaction.TransactionType.EXPENSE:
        account.balance -= transaction_amount
    account.save()


def update_account_balance_after_delete_transaction(account_id: int, transaction_amount):
    account = Account.objects.get(pk=account_id)
    account.balance += transaction_amount
    account.save()


def check_if_account_balance_exceed(account_balance, transaction_amount, transaction_type):
    if (transaction_type == Transaction.TransactionType.EXPENSE and
            account_balance < transaction_amount):
        raise ValueError(f'Transaction amount exceeds account balance , your balance is: {account_balance}$')
