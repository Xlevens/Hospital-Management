from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class DoctorViewSet(APIView):
  
    permission_classes = [IsAuthenticated]

    def get(self, request,pk=None):
        if pk:
            doctor = get_object_or_404(Doctor, id=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        else:
            doctor_objs = Doctor.objects.all()
            serializer = DoctorSerializer(doctor_objs, many=True)
            return Response(serializer.data)
       

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        serializer = DoctorSerializer(instance=doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        doctor.delete()
        return Response('Doctor deleted successfully!')

class PateintViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient_objs = Patient.objects.all()
        serializer = PatientSerializer(patient_objs, many = True)
        return Response(serializer.data)


    def post(self, request):
        
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
           
           serializer.save()
           return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


    def put(self, request, pk):
        patient = Patient.objects.get(id = pk)
        serializer = PatientSerializer(instance = patient, data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    def delete(self,request, pk):
        patient = Patient.objects.get(id = pk)
        patient.delete()
        return Response('Patient deleted successfully!')

class NurseViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        nurse_objs = Nurse.objects.all()
        serializer = NurseSerializer(nurse_objs, many = True)
        return Response(serializer.data)
 
    def post(self,request):
        serializer = NurseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
 
    def put(self,request, pk):
        nurse = Nurse.objects.get(id = pk)
        serializer = NurseSerializer(instance = nurse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
   
    def delete(self,request, pk):
        nurse = Nurse.objects.get(id = pk)
        nurse.delete()
        return Response('Nurse deleted successfully!')
    def get(self, request, pk):
        nurse = get_object_or_404(Nurse, id=pk)
        serializer = NurseSerializer(nurse)
        return Response(serializer.data)
class StaffViewSet(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request):
        staff_objs = Staff.objects.all()
        serializer = StaffSerializer(staff_objs, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StaffSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
   
    def put(self,request, pk):
        staff = Staff.objects.get(id = pk)
        serializer = StaffSerializer(instance = staff, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
 
    def delete(self,request, pk):
        staff = Staff.objects.get(id = pk)
        staff.delete()
        return Response('Staff deleted successfully!')
    def get(self, request, pk):
        staff = get_object_or_404(Staff, id=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
class AppointmentViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        appointment_objs = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment_objs, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AppointmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self,request, pk):
        appointment = Appointment.objects.get(id = pk)
        serializer = AppointmentSerializer(instance = appointment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    def delete(self,request, pk):
        appointment = Appointment.objects.get(id = pk)
        appointment.delete()
        return Response('Appointment deleted successfully!')
class PrescriptionViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        prescription_objs = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescription_objs, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PrescriptionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self,request, pk):
        prescription = Prescription.objects.get(id = pk)
        serializer = PrescriptionSerializer(instance = prescription, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)