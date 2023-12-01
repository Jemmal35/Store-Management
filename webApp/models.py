from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.first_name+' '+ self.user.last_name




class Product(models.Model):
    # ID = models.CharField(max_length=15)
    Name = models.CharField(max_length=200)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Entrance_Date = models.DateField(auto_now= True)
    Expired_Date = models.DateField(auto_now= True)
    Approved_By = models.CharField(max_length= 200 )
    Total_Price = models.FloatField(default=0)

    class Meta:
        ordering = ['Entrance_Date']
        db_table = 'products'


    def __str__(self):
        return self.Name 
    

class Solled(models.Model):
    Id = models.BigAutoField(primary_key= True)
    Name = models.CharField(max_length=200)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Solled_Date = models.DateField(auto_now= True)
    Solled_By = models.CharField(max_length= 200 )
    Total_Price = models.FloatField(default=0)

    class Meta:
        ordering = ['Solled_Date']
        db_table = 'solled_products'

    def __str__(self):
        return self.Name 
     

class DeletedProduct(models.Model):
    Id = models.BigAutoField(primary_key= True)
    Name = models.CharField(max_length=200)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Deleted_Date = models.DateField(auto_now= True)
    
    Deleted_By = models.CharField(max_length= 200 )
    Total_Price = models.FloatField(default=0)

    class Meta:
        ordering = ['Deleted_Date']
        db_table = 'deleted_products'
    

    def __str__(self):
        return self.Name + ', Deleted By: ' + str(self.Deleted_By)