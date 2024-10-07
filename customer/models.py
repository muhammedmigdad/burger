from django.db import models


ADDRES_TYPE_CHOICES = {
    ('home', 'home'),
    ('work', 'work'),
    ('other', 'other')
}

from users.models import User
from restaurant.models import *






class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "customer_customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email
    
    

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "customer_cart"
        verbose_name = "cart"
        verbose_name_plural = "carts"
        ordering = ["-id"]

    def __str__(self):
        
        return self.customer.user.email
    
class  CartBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey('customer.address', on_delete=models.SET_NULL, null=True, blank=True)
    item_total = models.FloatField()
    offer_amount = models.FloatField()
    totel_amount = models.FloatField()
    delivery_charge = models.FloatField()
    
    
    class Meta:
        db_table = "customer_cartbill"
        verbose_name = "cartbill"
        verbose_name_plural = "cartbills"
        ordering = ["-id"]

    def __str__(self):
        return self.customer.user.email
    
    
class Offer(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField()
    short_description = models.CharField(max_length=255)
    is_percentage = models.BooleanField()
    
    
    class Meta:
        db_table = "customer_offer"
        verbose_name = "offer"
        verbose_name_plural = "offers"
        ordering = ["-id"]

    def __str__(self):
        return self.code
    
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    appartment = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    address_type = models.CharField(max_length=255,choices=ADDRES_TYPE_CHOICES)
    
    
    class Meta:
        db_table = "customer_address"
        verbose_name = "address"
        verbose_name_plural = "addreses"
        ordering = ["-id"]

    def __str__(self):
        return self.landmark
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey('customer.address', on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.CharField(max_length=255)
    item_total = models.FloatField()
    offer_amount = models.FloatField()
    cartbill = models.ManyToManyField('customer.orderbill')
    totel_amount = models.FloatField()
    delivery_charge = models.FloatField()
    appartment = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255, choices=ADDRES_TYPE_CHOICES)
    
    class Meta:
        db_table = "customer_order"
        verbose_name = "order"
        verbose_name_plural = "orders"
        ordering = ["-id"]
    
    def __str__(self):
        return self.customer.user.email



class OrderBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "customer_orderbill"
        verbose_name = "orderbill"
        verbose_name_plural = "orderbills"
        ordering = ["-id"]

    def __str__(self):
        
        return self.customer.user.email