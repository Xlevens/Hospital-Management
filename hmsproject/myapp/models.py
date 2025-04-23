from django.db import models

# Create your models here.
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
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Nurse(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    assigned_doc = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True,related_name="nurses")
    def __str__(self):
        return self.name
class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True,related_name="patients")
    nurses = models.ManyToManyField(Nurse,blank=True,related_name="patients")
    def __str__(self):
        return self.name
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, default='Scheduled')
    def __str__(self):
        return self.patient.name + " - " + self.doctor.name + " - " + str(self.date) + " " + str(self.time)
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE,related_name="prescription")
    medication = models.TextField()
    dosage = models.TextField()
    instructions = models.TextField()
    def __str__(self):
        return self.appointment.patient.name + " - " + self.appointment.doctor.name
