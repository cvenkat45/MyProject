from src import views
from django.urls import path

app_name = 'Products'
urlpatterns = [
    path('api', views.srcindex, name="srcindex"),
    path('api/products/', views.products_api, name="products_api"),
    path('api/products/add/', views.add_product_api, name="add_product_api"),
    path('api/products/<int:pk>/', views.products_details_api, name="products_details_api"),
    path('api/products/edit/<int:pk>/', views.edit_product_api, name="edit_product_api"),
    path('api/products/delete/<int:pk>/', views.delete_product_api, name="delete_product_api"),
]
