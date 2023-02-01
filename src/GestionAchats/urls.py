from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/category', add_category, name='add_category'),
    path('delete/category/<int:pk>/', delete_category, name='delete_category'),
    path('categories', category_list, name='category_list'),
    path('add/product', add_product, name='add_product'),
    path('delete/product/<int:pk>/', delete_product, name='delete_product'),
    path('products', product_list, name='product_list'),
    path('add/client', add_client, name='add_client'),
    path('delete/client/<int:pk>/', delete_client, name='delete_client'),
    path('clients', client_list, name='client_list'),
    path('add/order', add_order, name='add_order'),
    path('delete/order/<int:pk>/', delete_order, name='delete_order'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('orders', list_order, name='list_order'),
    path('add/product/order/<int:pk>/', add_products_order, name='add_product_order'),
    path('orders/<str:name>/', orders_by_customer, name='orders_by_customer'),
    path('register', create_user, name='create_user'),
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('users', user_list, name='user_list'),
    path('delete/user/<int:pk>/', delete_user, name='delete_user'),
    path('search', search_orders, name='search_orders'),
    path('login/', LoginPageView.as_view(), name='login'),

    

]
