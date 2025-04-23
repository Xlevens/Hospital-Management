from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        
        exclude = ['id']
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        
        exclude = ['id']
class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        
        exclude = ['id']
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        
        exclude = ['id']
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        
        exclude = ['id']
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        
        exclude = ['id']