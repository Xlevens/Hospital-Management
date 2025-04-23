from django.urls import path
from . import views
urlpatterns = [
  
    path('doctor', views.DoctorViewSet.as_view()),
    path('doctor/<int:pk>', views.DoctorViewSet.as_view()),
    path('patient', views.PateintViewSet.as_view()),
    path('patient/<int:pk>', views.PateintViewSet.as_view()),
    path('nurse', views.NurseViewSet.as_view()),
    path('nurse/<int:pk>', views.NurseViewSet.as_view()),
    path('staff', views.StaffViewSet.as_view()),
    path('staff/<int:pk>', views.StaffViewSet.as_view()),
    path('appointment', views.AppointmentViewSet.as_view()),
    path('appointment/<int:pk>', views.AppointmentViewSet.as_view()),
    path('prescription', views.PrescriptionViewSet.as_view()),
    path('prescription/<int:pk>', views.PrescriptionViewSet.as_view()),
    
]