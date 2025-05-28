
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:product_id>/', views.edit_products, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_products, name='delete_product'),
    
]