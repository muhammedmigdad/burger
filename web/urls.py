from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
   path("", views.index, name="index"),
   path("login/", views.login, name="login"),
   path("register/", views.register, name="register"),
   path("logout/", views.logout, name="logout"),
   path("restaurants/<int:id>/", views.restaurants, name="restaurants"),
   path("single_rest/<int:id>/", views.single_rest, name="single_rest"),
   path("cart/", views.cart, name="cart"),
   path("add_cart/<int:id>/", views.add_cart, name="add_cart"),
   path("cart_plus/<int:id>/", views.cart_plus, name="cart_plus"),
   path("cart_minus/<int:id>/", views.cart_minus, name="cart_minus"),   
   path("add_address/", views.add_address, name="add_address"),
   path("address/", views.address, name="address"),
   path("offer/", views.offer, name="offer"),
   path("checkout/", views.checkout, name="checkout"),   
   path("order/", views.order, name="order"), 
   path('validate_email/', views.validate_email, name='validate_email'),
   path("account/", views.account, name="account"),
   path("single_order/<int:id>/", views.single_order, name="single_order"), 
   path("creat_order/", views.creat_order, name="creat_order"),     
   path('address/delete/<int:id>/', views.address_delete,name="address_delete"),
   path('address/edit/<int:id>/', views.address_edit,name="address_edit"),
   path('address/select/<int:id>/', views.address_select,name="address_select"),
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
]
