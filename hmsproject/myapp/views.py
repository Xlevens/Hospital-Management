from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def doctor(request):
    doctor_objs = Doctor.objects.all()
    serializer = DoctorSerializer(doctor_objs, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def post_doc(request):
    serializer = DoctorSerializer(data = request.data)
    if serializer.is_valid():
     serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def update_doc(request, pk):
    doctor = Doctor.objects.get(id = pk)
    serializer = DoctorSerializer(instance = doctor, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_doc(request, pk):
    doctor = Doctor.objects.get(id = pk)
    doctor.delete()
    return Response('Doctor deleted successfully!')
api_view(['GET'])
def patient(request):
    patient_objs = Patient.objects.all()
    serializer = PatientSerializer(patient_objs, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def post_patient(request):
    print("REQUEST DATA:", request.data)
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        print("VALIDATED DATA:", serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=201)
    print("ERRORS:", serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_patient(request, pk):
    patient = Patient.objects.get(id = pk)
    serializer = PatientSerializer(instance = patient, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_patient(request, pk):
    patient = Patient.objects.get(id = pk)
    patient.delete()
    return Response('Patient deleted successfully!')

@api_view(['GET'])
def nurse(request):
    nurse_objs = Nurse.objects.all()
    serializer = NurseSerializer(nurse_objs, many = True)
    return Response(serializer.data)
@api_view(['POST'])
def post_nurse(request):
    serializer = NurseSerializer(data = request.data)
    if serializer.is_valid():
     serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def update_nurse(request, pk):
    nurse = Nurse.objects.get(id = pk)
    serializer = NurseSerializer(instance = nurse, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_nurse(request, pk):
    nurse = Nurse.objects.get(id = pk)
    nurse.delete()
    return Response('Nurse deleted successfully!')
@api_view(['GET'])
def staff(request):
    staff_objs = Staff.objects.all()
    serializer = StaffSerializer(staff_objs, many = True)
    return Response(serializer.data)
@api_view(['POST'])
def post_staff(request):
    serializer = StaffSerializer(data = request.data)
    if serializer.is_valid():
     serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def update_staff(request, pk):
    staff = Staff.objects.get(id = pk)
    serializer = StaffSerializer(instance = staff, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_staff(request, pk):
    staff = Staff.objects.get(id = pk)
    staff.delete()
    return Response('Staff deleted successfully!')