from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_sold')


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, through='CartProduct')


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
