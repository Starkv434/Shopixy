from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from user_accounts.models import Profile



CATEGORY_CHOICES = [
    ('Curd', 'Curd'),
    ('Milk', 'Milk'),
    ('Paneer', 'Paneer'),
    ('Ghee', 'Ghee'),
    ('Kulfi', 'Kulfi'),
    ('Ice', 'Ice-Creams'),
    ('Milkshake', 'Milkshake'),
]

# Create your models here.
class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    selling_price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    description = models.TextField()
    quantity = models.CharField(max_length=1000, null=True, blank=True)
    composition = models.TextField(default="")
    category = models.CharField(max_length=50, choices = CATEGORY_CHOICES)
    prod_image = models.ImageField(upload_to="prod_img")
    
    
    def __str__(self):
        return self.product_name
    
class Cart(BaseModel):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    no_of_items = models.IntegerField(default=1)
    
    @property
    def total_cost(self):
        if self.product.discounted_price == 0:
            value = self.product.selling_price
        else:
            value = self.product.discounted_price
        return self.no_of_items * value
    

class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=50, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=50, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=50, blank=True, null=True)
    paid = models.BooleanField(default=False)
    
  
    
    

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)
    
    
class OrderPlaced(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name="profile", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    no_of_items = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Accepted")
    
    @property
    def total_cost(self):
        if self.product.discounted_price == 0:
            value = self.product.selling_price
        else:
            value = self.product.discounted_price
        return self.no_of_items * value
    
   

class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    