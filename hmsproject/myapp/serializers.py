from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ['id']
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # fields = '__all__'
        exclude = ['id']
class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        # fields = '__all__'
        exclude = ['id']
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        # fields = '__all__'
        exclude = ['id']