from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=30)
    gender = models .CharField(max_length=10)
    age = models.IntegerField()
    image = models.ImageField(blank=True, upload_to="image")

    password = models.CharField(max_length=20, default=None, null=True)
