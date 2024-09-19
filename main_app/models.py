from django.db import models

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
        



 