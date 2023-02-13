from django.contrib import admin
from .models import Buyer, Seller, User, Product, CartProduct, Cart, OrderProduct, Category, Order



class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")

    @staticmethod
    def user_info(obj):
        if obj.user:
            return "{}".format("".join(list(obj.user.first_name, obj.user.last_name)))


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(OrderProduct)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
