from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name

   class Meta:
       verbose_name_plural = "Categories"

class Product(models.Model):
   name = models.CharField(max_length=200)
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
   stock = models.IntegerField(default=0)
   image_url = models.CharField(max_length=255, null=True, blank=True)  # Almacena la URL de la imagen
   is_active = models.BooleanField(default=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name