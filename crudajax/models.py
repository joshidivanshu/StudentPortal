from django.db import models

# Create your models here.
class Teacher(models.Model):
    eno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=30)
    experience = models.IntegerField()

