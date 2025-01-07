from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from accounts.form import AccountForm
from accounts.models import Account


def index(request):
    accounts = Account.objects.order_by('-id')

    return render(request, 'accounts/index.html', {'accounts': accounts})


def create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            messages.success(request, 'Account created successfully!')
            return redirect('account-index')

    form = AccountForm()
    return render(request, 'accounts/create.html', {'form': form})


def update(request, account_id: int):
    account = get_object_or_404(Account, pk=account_id)
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        account = form.save(commit=False)
        account.user = request.user
        account.save()
        messages.success(request, 'Account updated successfully!')
        return redirect('account-index')

    return render(request, 'accounts/edit.html', {'form': form, 'account': account})
