from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ItemDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150,default='False')
    total=models.FloatField()
    datel=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)


class Cart(models.Model):
    id_product=models.IntegerField()
    id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    
class Cart(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)
