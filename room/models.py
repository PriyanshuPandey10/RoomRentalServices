from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username

class Room(models.Model):
    room_no=models.CharField(max_length=10,null=True)
    price=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)


class Booked(models.Model):
    full_name=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=20,null=True)
    contact2=models.CharField(max_length=20,null=True)
    bookint_date=models.CharField(max_length=20,null=True)
    days=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=20,null=True)
    dob=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)


class Contact(models.Model):
    c_name=models.CharField(max_length=20,null=True)
    c_email=models.CharField(max_length=20,null=True)
    c_mobile=models.CharField(max_length=20,null=True)
    c_purpose=models.CharField(max_length=20,null=True)

