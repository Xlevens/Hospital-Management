from django.urls import path
from . import views

urlpatterns = [
    path('doctor', views.DoctorViewSet.as_view(), name='doctor-list'),
    path('doctor/<int:pk>', views.DoctorViewSet.as_view(), name='doctor-detail'),

    path('patient', views.PateintViewSet.as_view(), name='patient-list'),
    path('patient/<int:pk>', views.PateintViewSet.as_view(), name='patient-detail'),

    path('nurse', views.NurseViewSet.as_view(), name='nurse-list'),
    path('nurse/<int:pk>', views.NurseViewSet.as_view(), name='nurse-detail'),

    path('staff', views.StaffViewSet.as_view(), name='staff-list'),
    path('staff/<int:pk>', views.StaffViewSet.as_view(), name='staff-detail'),

    path('appointment', views.AppointmentViewSet.as_view(), name='appointment-list'),
    path('appointment/<int:pk>', views.AppointmentViewSet.as_view(), name='appointment-detail'),

    path('prescription', views.PrescriptionViewSet.as_view(), name='prescription-list'),
    path('prescription/<int:pk>', views.PrescriptionViewSet.as_view(), name='prescription-detail'),
]