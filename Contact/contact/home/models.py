from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Category(models.Model):
 name=models.CharField(max_length=255)
 class Meta:
   ordering=("name",)
   verbose_name_plural="categories"
 def __str__(self):
  return self.name
class Item(models.Model):
 name=models.CharField(max_length=255)
 address=models.TextField(blank=True,null=True)
 gmail=models.CharField(max_length=255)
 phone_number=models.CharField(max_length=13)
 created_by = models.ForeignKey(User, related_name="item", on_delete=models.CASCADE)
 def __str__(self):
  return self.name
