from datetime import datetime

from django.db import models


# Create your models here.
class UserSignUp(models.Model):
    # created_dt=models.DateTimeField(auto_now_add=True) #auto_now_add returns true date but return false time 
    #to solve this need to change time zone in settings.py
    #another way
    created_dt=models.DateTimeField(default=datetime.now(),blank=True)
    FName=models.CharField(max_length=20)
    LName=models.CharField(max_length=20)
    UNm=models.EmailField()
    PWD=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class mynotes(models.Model):
    qry_title=models.CharField(max_length=200)
    qry_cate=models.CharField(max_length=100)
    myfiles=models.FileField(upload_to='myNotes')
    comments=models.TextField()
    submitted_user=models.EmailField(null=True)
    
class feedback(models.Model):
    created_dt=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    subject=models.TextField()
    msg=models.TextField()


    