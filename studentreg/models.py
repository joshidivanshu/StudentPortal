from django.db import models

#Create your models here.
#add dob
#identify 18+. count signal.
#name


class Student(models.Model):
    eno = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.eno} {self.fname} {self.lname}'
