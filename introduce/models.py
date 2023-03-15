from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    image = models.ImageField(blank=True, upload_to="image")
    address = models.CharField(max_length=100, null=True)
    job = models.CharField(max_length=100, null=True)
    cellphone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=100, null=True)
    hobby = models.CharField(max_length=50, null=True)

    password = models.CharField(max_length=20,  null=True)
