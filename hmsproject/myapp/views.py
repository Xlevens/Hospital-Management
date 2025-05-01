from django.shortcuts import render, get_object_or_404 
from .models import *
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def api_home(request):
    return Response({
        "Doctors (List/Create)": request.build_absolute_uri(reverse('doctor-list')),
        "Patients (List/Create)": request.build_absolute_uri(reverse('patient-list')),
        "Nurses (List/Create)": request.build_absolute_uri(reverse('nurse-list')),
        "Staff (List/Create)": request.build_absolute_uri(reverse('staff-list')),
        "Appointments (List/Create)": request.build_absolute_uri(reverse('appointment-list')),
        "Prescriptions (List/Create)": request.build_absolute_uri(reverse('prescription-list')),
    })


class DoctorViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
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

    def patch(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        serializer = DoctorSerializer(instance=doctor, data=request.data, partial=True)
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

    def get(self, request, pk=None):
        if pk:
            patient = get_object_or_404(Patient, id=pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        else:
            patient_objs = Patient.objects.all()
            serializer = PatientSerializer(patient_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        patient = Patient.objects.get(id=pk)
        serializer = PatientSerializer(instance=patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        patient = Patient.objects.get(id=pk)
        patient.delete()
        return Response('Patient deleted successfully!')


class NurseViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            nurse = get_object_or_404(Nurse, id=pk)
            serializer = NurseSerializer(nurse)
            return Response(serializer.data)
        else:
            nurse_objs = Nurse.objects.all()
            serializer = NurseSerializer(nurse_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        nurse = Nurse.objects.get(id=pk)
        serializer = NurseSerializer(instance=nurse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        nurse = Nurse.objects.get(id=pk)
        nurse.delete()
        return Response('Nurse deleted successfully!')


class StaffViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            staff = get_object_or_404(Staff, id=pk)
            serializer = StaffSerializer(staff)
            return Response(serializer.data)
        else:
            staff_objs = Staff.objects.all()
            serializer = StaffSerializer(staff_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        staff = Staff.objects.get(id=pk)
        serializer = StaffSerializer(instance=staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        staff = Staff.objects.get(id=pk)
        staff.delete()
        return Response('Staff deleted successfully!')


class AppointmentViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            appointment = get_object_or_404(Appointment, id=pk)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
        else:
            appointment_objs = Appointment.objects.all()
            serializer = AppointmentSerializer(appointment_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        serializer = AppointmentSerializer(instance=appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment.delete()
        return Response('Appointment deleted successfully!')


class PrescriptionViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            prescription = get_object_or_404(Prescription, id=pk)
            serializer = PrescriptionSerializer(prescription)
            return Response(serializer.data)
        else:
            prescription_objs = Prescription.objects.all()
            serializer = PrescriptionSerializer(prescription_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        prescription = Prescription.objects.get(id=pk)
        serializer = PrescriptionSerializer(instance=prescription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        prescription = Prescription.objects.get(id=pk)
        prescription.delete()
        return Response('Prescription deleted successfully!')


class DepartmentViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            department = get_object_or_404(Department, id=pk)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        else:
            department_objs = Department.objects.all()
            serializer = DepartmentSerializer(department_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        department = Department.objects.get(id=pk)
        department.delete()
        return Response('Department deleted successfully!')


class RoomViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            room = get_object_or_404(Room, id=pk)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        else:
            room_objs = Room.objects.all()
            serializer = RoomSerializer(room_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(instance=room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        room = Room.objects.get(id=pk)
        room.delete()
        return Response('Room deleted successfully!')


class BillViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            bill = get_object_or_404(Bill, id=pk)
            serializer = BillSerializer(bill)
            return Response(serializer.data)
        else:
            bill_objs = Bill.objects.all()
            serializer = BillSerializer(bill_objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        bill = Bill.objects.get(id=pk)
        serializer = BillSerializer(instance=bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        bill = Bill.objects.get(id=pk)
        bill.delete()
        return Response('Bill deleted successfully!')
