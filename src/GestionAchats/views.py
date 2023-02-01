from django.shortcuts import *
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


@login_required
def home(request):
    return render(request, 'achats/home.html')

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'achats/category_list.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'achats/add_category.html', {'form': form})

@login_required
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'achats/product_list.html', {'products': products})

@login_required
def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'achats/add_product.html', {'form': form, 'categories' : categories})

@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'achats/client_list.html', {'clients': clients})

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'achats/add_client.html', {'form': form})

@login_required
def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('client_list')

@login_required
def add_order(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            productId = request.POST['product']
            product = Product.objects.get(id=productId)
            quantity = request.POST['quantity']
            orderProduct = OrderProduct.objects.create(order=order, product=product, quantity=quantity)
            orderProduct.save()
            order.total_price = order.get_total_price()
            order.save()
            return redirect('list_order')
        else:
            print("Form not valid")
            print(form.errors)
    else:
        form = OrderForm()
    return render(request, 'achats/add_order.html', {'form': form, 'clients' : clients, 'products' : products})

@login_required
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('list_order')

@login_required
def add_products_order(request, pk):
    products = Product.objects.all()
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            productId = request.POST['product']
            product = Product.objects.get(id=productId)
            quantity = request.POST['quantity']
            orderProduct = OrderProduct.objects.create(order=order, product=product, quantity=quantity)
            orderProduct.save()
            order.total_price = order.get_total_price()
            order.save()
            return redirect('order_detail', pk)
        else:
            print("Form not valid")
            print(form.errors)
    else:
        form = OrderProductForm()
    return render(request, 'achats/add_product_order.html', {'form': form, 'order': order, 'products' : products})

@login_required
def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'achats/order_detail.html', {'order': order})

@login_required
def list_order(request):
    orders = Order.objects.all()
    return render(request, 'achats/list_order.html', {'orders': orders})

@login_required
def orders_by_customer(request, name):
    orders = Order.get_orders_by_customer_name(name)
    return render(request, 'achats/orders.html', {'orders': orders, 'name' : name})

@login_required
def search_orders(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        return orders_by_customer(request, customer_name)
    else:
        return render(request, 'achats/home.html')

@login_required
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'achats/create_user.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'achats/user_list.html', {'users': users})

@login_required
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'username or password not correct')
                return redirect('user_login')
    else:
        form = AuthenticationForm()
    return render(request, 'achats/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

class LoginPageView(LoginView):
    template_name = 'achats/login.html'


