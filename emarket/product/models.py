from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
class Categorie(models.TextChoices):
     computer="Computer"
     clothes="Clothes"
     food="Food"
     Home="Home"
     
class product(models.Model):
    name = models.CharField(max_length=50,blank=False)
    description=models.TextField(max_length=250,blank=False)
    price=models.DecimalField(max_digits=10, decimal_places=2,blank=False)    
    brand = models.CharField(max_length=50,blank=False)
    categorie= models.CharField(max_length=50,choices=Categorie.choices,blank=False)
    rate=models.DecimalField(max_digits=10,decimal_places=2,blank=False)  
    stock=models.IntegerField()
    created_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)      
   
   
class review(models.Model):
    product=models.ForeignKey(product, null=True, on_delete=models.CASCADE, related_name="reviews")
    rating=models.IntegerField(default=0)
    name = models.CharField(max_length=50,blank=False)
    comments=models.TextField(max_length=250,blank=False)
    created_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)      
    
    def __str__(self) :
        return self.comments