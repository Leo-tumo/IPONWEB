from django.contrib import admin

#
from .models import StoreCategory, ItemCategory, Customer, Item, \
    StoreOwner, Store, MyBag, Purchase


#


@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registered_at']


@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registered_at']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'store_category']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'price', 'quantity', 'info', 'store']


@admin.register(MyBag)
class MyBagAdmin(admin.ModelAdmin):
    list_display = ['customer', 'products', 'total_price']

    @staticmethod
    def products(obj):
        return "\n".join([p.name for p in obj.items.all()])


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'items_display', 'total_price']

    def items_display(self, obj):
        return ', '.join([item.name for item in obj.items.all()])

    items_display.short_description = 'Items'

