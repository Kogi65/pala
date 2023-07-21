from django.db import models

class Order(models.Model):
    As_at= models.DateTimeField(auto_now_add=True)
    serial_no= models.CharField(max_length=9, primary_key=True)   
    category= models.CharField(max_length=25) 
    weight=models.IntegerField() 
    quantity= models.IntegerField() 
    shipping_status=models.CharField(max_length=15) 

    def __str__(self):
        pass
