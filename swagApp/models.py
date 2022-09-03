from django.db import models


class Akshay(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

class zara(models.Model):
    user=models.CharField(max_length=20)
    phone=models.IntegerField()

class login(models.Model):
    usern=models.CharField(max_length=20)
    pswd=models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    designation=models.CharField(max_length=100)
    salary=models.IntegerField()

class college(models.Model):
    Name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    mark=models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)