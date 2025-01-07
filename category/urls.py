from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.index, name='category-index'),
    path('category/create/', views.create, name='create-category'),
    path('category/update/<int:category_id>', views.update, name='update-category'),
]
