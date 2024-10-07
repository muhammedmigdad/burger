from django import forms
from restaurant.models import *
from users.models import User
from customer.models import *




class StoreCategoryform(forms.ModelForm):
    class Meta:
        model = StoreCategory
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'category name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
class Storeform(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'category', 'image', 'taglin', 'rating', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}), 
            'taglin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tagline'}),  
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
            'time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
        }

class SliderForm(forms.ModelForm):  
    class Meta:
        model = Slider
        fields = ['name', 'image', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slider Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class FoodCategoryform(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'is_veg', 'image', 'foodcategory']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'is_veg': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'foodcategory': forms.Select(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'is_customer', 'is_store', 'is_agent', 'is_manager']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'is_customer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_store': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_agent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['code', 'discount', 'short_description', 'is_percentage']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Code'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount Amount'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short Description'}),
            'is_percentage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'address',
            'order_id',
            'item_total',
            'offer_amount',
            'totel_amount',
            'delivery_charge',
        ]
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order ID'}),
            'item_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Item Total'}),
            'offer_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Offer Amount'}),
            'totel_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Amount'}),
            'delivery_charge': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Charge'}),
        }
        
class ManagerLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )