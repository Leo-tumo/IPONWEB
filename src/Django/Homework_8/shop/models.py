from django.db import models
from django.contrib.auth.models import User


class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='store_category_images')


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='item_category_images')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer_avatars')
    registered_at = models.DateTimeField(auto_now_add=True)


class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='store_owner_avatars')
    registered_at = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='item_images')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    info = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.FloatField()


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()


