from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ContactInfo(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField(max_length=300)
    Phone=models.CharField(max_length=14,null=True,blank=True)
    Subject=models.CharField(max_length=300)
    Message=models.TextField()

    class Meta:
        verbose_name_plural=("ContactInfos")
    def __str__(self):
        return self.Name
        

class Banner(models.Model):
    Name=models.CharField(max_length=300)
    Image=models.ImageField(upload_to="media")
    product_name=models.CharField(max_length=400,null=True,blank=True)
    Price=models.CharField(max_length=100)
    dis_price=models.CharField(max_length=14,null=True,blank=True)

    class Meta:
        verbose_name_plural=("Banner")
    def __str__(self):
        return self.Name

class Category (models.Model):
    name=models.CharField(max_length=50, null=False)
    img =models.ImageField(upload_to='category_images/',blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural=("Category")
    def __str__(self):
        return self.name
        

class Brand(models.Model):
    name=models.CharField(max_length=50,null=False)
    img = models.ImageField(upload_to='category_images/',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural=("Brand")
    def __str__(self):
        return self.name
        
class Product(models.Model):
    name=models.CharField(max_length=400)
    image= models.ImageField(upload_to='ProductImage')
    regular_price=models.PositiveIntegerField()
    discount_price=models.PositiveIntegerField(blank=True,null=True)
    descriptions=models.TextField(null=True)
    additional_descriptions=models.TextField(blank=True,null=True)
    stock=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural=("Products")
    def __str__(self):
        return self.name
        

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    added_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

        
        
class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"{self.user.username}'s wishlist - {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('processing','Processing'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    )
     
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Product, through='OrderItem')
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
       
class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    city=models.CharField( max_length=100)
    state=models.CharField(max_length=100)
    delivery_area=models.CharField(max_length=20, choices=[('inside_dhaka', 'Inside Dhaka'),('outside_dhaka', 'Outside Dhaka')])
    
    def __str__(self):
        return f"{self.user.username} - {self.address}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOIES = (
        ('credit_card' , 'Credit Card'),
        ('paypal','PayPal'),
        ('bank_transfer','Bank Transfer'),
    )
    
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOIES)
    transaction_id=models.CharField(max_length=100, unique=True,null=True)
    status=models.CharField(max_length=50, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"