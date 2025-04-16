from django.contrib import admin


# Register your models here.

from .models import Staff, Doctor, Nurse, Patient

admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)