from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    is_dealer=models.BooleanField(default=False)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=12)
    dob = models.DateField(default=datetime.now, blank=True)
    image=models.ImageField(upload_to='basim',null=True)


class District(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Area(models.Model):
    district_name=models.ForeignKey(District,on_delete=models.CASCADE)
    area_name=models.CharField(max_length=25)

    def __str__(self):
        return self.district_name


class Book(models.Model):
    book_name=models.CharField(max_length=30)
    prize=models.CharField(max_length=25)
    author=models.CharField(max_length=30)
    date=models.DateTimeField(default=datetime.now, blank=True)
    image=models.ImageField(upload_to='basim',null=True)

    def __str__(self):
        return self.book_name


class Book_Category(models.Model):
    category_name=models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=100)
    replay=models.CharField(max_length=100,null=True)
    date=models.DateField(null=True)

    def __str__(self):
        return self.feedback

