from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from category.form import CategoryForm
from category.models import Category


def index(request):
    categories = Category.objects.all()

    return render(request, 'category/index.html', {'categories': categories})


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category-index')

    form = CategoryForm()
    return render(request, 'category/create.html', {'form': form})


def update(request, category_id: int):
    category = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        messages.success(request, 'Category updated successfully!')
        return redirect('category-index')

    return render(request, 'category/edit.html', {'form': form, 'category': category})
