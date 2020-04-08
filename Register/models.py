from django.db import models

# Create your models here.
class register(models.Model):
    Username=models.CharField(max_length=100)
    ContactInfo =models.IntegerField()
    Password= models.CharField(max_length=10)
    ConfrimPassword=models.CharField(max_length=10)
    FullName=models.TextField(max_length=100)

  
    

class items(models.Model):
    ItemName=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    Date=models.DateField()
    Total=models.IntegerField()


    
    
    


