from django.db import models


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')
    
    
    
    class meta:
           db_table = "restaurant_store_category"
           verbose_name = "store_category"
           verbose_name_plural = "store_categories"
           ordering = ['-id']
    
    
    def __str__(self):
          return self.name



class Store(models.Model):
    name =  models.CharField(max_length=100)
    category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store')
    taglin = models.CharField(max_length=255)
    rating = models.FloatField()
    time = models.IntegerField()
    
    
    class meta:
        db_table = "restaurant_store"
        verbose_name = "store"
        verbose_name_plural = "stores"
        ordering = ['-id']
    
    
    def __str__(self):
        return self.name
    
    
class Slider(models.Model):
    name =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')
    store= models.ForeignKey(Store, on_delete=models.CASCADE)
    
    
    class meta:
        db_table = "restaurant_slider"
        verbose_name = "slider"
        verbose_name_plural = "sliders"
        ordering = ['-id']
    
    
    def __str__(self):
        return self.name
    
class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    
    
        
    class meta:
        db_table = "foodcategory"
        verbose_name = "foodcategory"
        verbose_name_plural = "foodcategories"
        ordering = ['-id']
    
    
    def __str__(self):
        return self.name
    
    
class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    is_veg = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Food")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    foodcategory = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    
    
    
    
    
    class meta:
        db_table = "food"
        verbose_name = "food"
        verbose_name_plural = "foods"
        ordering = ['-id']
    
    
    
    
    def __str__(self):
        return self.name
    