from django.urls import path
from manager import views

app_name = "manager"

urlpatterns = [
    
   path("", views.index, name="index"),
   path("login/", views.login, name="login"),
   path("logout/", views.logout, name="logout"),
   path("store_categories/", views.store_categories, name="store_categories"),
   path("store_category/add", views.store_category_add, name="store_category_add"),
   path("store_category_edit/<int:id>/", views.store_category_edit, name="store_category_edit"),
   path("store_category_delete/<int:id>/", views.store_category_delete, name="store_category_delete"),
   path("store/", views.store, name="store"),
   path("store_add", views.store_add, name="store_add"),
   path("store_edit/<int:id>/", views.store_edit, name="store_edit"),
   path("store_delete/<int:id>/", views.store_delete, name="store_delete"),
   path("food/", views.food, name="food"),
   path('food_add/', views.food_add, name='food_add'),
   path("food_edit/<int:id>/", views.food_edit, name="food_edit"),
   path("food_delete/<int:id>/", views.food_delete, name="food_delete"),
   path("food_categories/", views.food_categories, name="food_categories"),
   path("food_category_add/", views.food_category_add, name="food_category_add"),
   path("food_category_edit/<int:id>/", views.food_category_edit, name="food_category_edit"),
   path("food_category_delete/<int:id>/", views.food_category_delete, name="food_category_delete"),
   path("order/", views.order, name="order"),
   path("users/", views.users, name="users"),
   path("users_delete/<int:id>/", views.users_delete, name="users_delete"),
   path("users_edit/<int:id>/", views.users_edit, name="users_edit"),
   path("users_add/", views.users_add, name="users_add"),
   # path("customer/", views.customer, name="customer"),
   path("offers/", views.offers, name="offers"),
   path("offers_add", views.offers_add, name="offers_add"),
   path("offers_edit/<int:id>/", views.offers_edit, name="offers_edit"),
   path("offers_delete/<int:id>/", views.offers_delete, name="offers_delete"),
   path("slider/", views.slider, name="slider"),
   path("slider_add", views.slider_add, name="slider_add"),
   path("slider_edit/<int:id>/", views.slider_edit, name="slider_edit"),
   path("slider_delete/<int:id>/", views.slider_delete, name="slider_delete"),  
   
]