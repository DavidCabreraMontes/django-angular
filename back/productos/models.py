from django.db import models

# Create your models here.

class productos(models.Model):
    name = models.CharField(max_length=150,null=False,unique=True)
    price = models.FloatField(null=False)
    stock= models.IntegerField()
 
    class Meta:
        db_table= "Productos"