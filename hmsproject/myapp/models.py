from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=255),
    email = models.EmailField(unique=True),
    department = models.CharField(max_length=100)
class Doctor(models.Model):
    name = models.CharField(max_length=255),
    email = models.EmailField(unique=True),
    specialization = models.CharField(max_length=100),
    department = models.CharField(max_length=100)
class Nurse(models.Model):
    name = models.CharField(max_length=255),
    email = models.EmailField(unique=True), 
    department = models.CharField(max_length=100)
    assigned-doc = models.ManyToManyField(Doctor, on_delete=models.SET_NULL),
class Patient(models.Model):
    name = models.CharField(max_length=255),
    email = models.EmailField(unique=True), 
    doctor = models.ManyToManyField(Doctor, on_delete=models.SET_NULL),
    nurses = models.ManyToManyField(Nurse,on_delete=models.SET_NULL )

