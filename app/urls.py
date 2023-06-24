from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('search/', views.search, name="search"),
    path('<str:category_name>/update-category/', views.updateCategory, name="update-category"),
    path('<str:supplier_name>/update-supplier/', views.updateSupplier, name="update-supplier"),
    path('<str:product_code>/update-product/', views.updateProduct, name="update-product"),

    path('<str:product_code>/remove-product/', views.removeProduct, name="remove-product"),

    path('<str:product_code>/product-detail/', views.productDetail, name="product-detail"),
    path('<str:category_name>/category-detail/', views.categoryDetail, name="category-detail"),
    path('<str:supplier_name>/supplier-detail/', views.supplierDetail, name="supplier-detail"),

    path('register-product/', views.registerProduct, name="register-product"),
    path('register-category/', views.registerCategory, name="register-category"),
    path('register-supplier/', views.registerSupplier, name="register-supplier"),
    path('', views.stock, name="stock"),
]