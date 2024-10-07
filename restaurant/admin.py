from django.contrib import admin

from restaurant.models import StoreCategory, Store, Slider, FoodCategory, Food


admin.site.register(StoreCategory)
admin.site.register(Store)
admin.site.register(Slider)
admin.site.register(FoodCategory)
admin.site.register(Food)
