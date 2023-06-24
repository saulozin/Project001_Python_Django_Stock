from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('search/', views.search, name="search"),
    path('', views.stock, name="stock"),
    path('register-product/', views.registerProduct, name="register-product"),
    path('<str:product_code>/update/', views.updateProduct, name="update-product"),
    path('<str:product_code>/remove-product/', views.removeProduct, name="remove-product"),
    path('<str:product_code>/detail/', views.productDetail, name="product-detail"),
]