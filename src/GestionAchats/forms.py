from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
    
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Client.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = models.IntegerField()

    class Meta:
        model = Order
        fields = ['customer','product']
        widget=forms.Select(attrs={'class': 'form-control'})

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = [ 'product', 'quantity']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)







