from django.urls import path
from . import views
urlpatterns = [
    path('accounts/', views.index, name='account-index'),
    path('accounts/create/', views.create, name='create-account'),
    path('accounts/update/<int:account_id>', views.update, name='update-account'),
]