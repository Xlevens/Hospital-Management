from django.db import models
from datetime import date,timezone,datetime
from django.utils import timezone
Choice = {("M","Male"), ("F","female")}
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True,related_name="doctors")
    gender = models.CharField(max_length=10, choices=Choice, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    def __str__(self):
        return "Dr."+self.name
class Nurse(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True,related_name="nurses")
    assigned_doc = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True,related_name="nurses")
    gender = models.CharField(max_length=10, choices=Choice, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.name
class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10,choices=Choice, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True,related_name="patients")
    nurses = models.ManyToManyField(Nurse,blank=True,related_name="patients")
    admitted_on = models.DateField(default=date.today)
    admitted_by = models.ForeignKey(Staff, on_delete=models.SET_NULL,null=True,related_name="patients")
    discharged_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Admitted')
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True,related_name="patients")

    
    def __str__(self):
        return self.name
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="appointments")
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.now)
    status = models.CharField(max_length=50, default='Scheduled')
   

    def __str__(self):
        return self.patient.name + " - " + self.doctor.name + " - " + str(self.date) + " " + str(self.time)
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE,related_name="prescription")
    medication = models.TextField()
    def __str__(self):
        return self.appointment.patient.name + " - " + self.appointment.doctor.name
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)  # e.g., ICU, General, Private
    occupied = models.BooleanField(default=False)
    def __str__(self):
        return self.room_number + " - " + self.type
class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.patient.name + " - " + str(self.total_amount) + " - " + str(self.date)
