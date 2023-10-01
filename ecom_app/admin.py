from django.contrib import admin
from .models import Product, Cart, OrderPlaced, Payment, Wishlist
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'selling_price', 'discounted_price', 'category', 'prod_image']
    
admin.site.register(Product, ProductsAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'no_of_items']
    
admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","profile","product","no_of_items","ordered_date","status"]

admin.site.register(OrderPlaced, OrderAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user","amount","razorpay_order_id","razorpay_payment_status","razorpay_payment_id","paid"]

admin.site.register(Payment, PaymentAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]

admin.site.register(Wishlist, WishlistAdmin)
