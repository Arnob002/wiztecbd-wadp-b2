from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CreateInfoModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.username}'
    
class TaskModel(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    STATUS=[
        ('Pending','Pending'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    ]
    status=models.CharField(choices=STATUS,max_length=100,null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.title}'
    
class ProfileModel(models.Model):
    
    user = models.OneToOneField(CreateInfoModel,on_delete=models.CASCADE,null=True,related_name='user_profile')
    address = models.TextField(null=True)
    contact = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.full_name}'
    
class ProductModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    qty = models.PositiveBigIntegerField(null=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    created_by = models.ForeignKey(CreateInfoModel,on_delete=models.CASCADE,related_name='user_product',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.name}'
    

