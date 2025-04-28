from django.contrib import admin


# Register your models here.

from .models import Staff, Doctor, Nurse, Patient, Appointment, Prescription,Department,Room

admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription) 
admin.site.register(Department)
admin.site.register(Room)