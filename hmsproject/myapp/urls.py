from django.urls import path
from . import views
urlpatterns = [
    path('add_doctor/', views.post_doc),
    path('doctor', views.doctor),
    path('update/<int:pk>/', views.update_doc),
    path('delete/<int:pk>/', views.delete_doc),
    path('add_patient/', views.post_patient),
    path('patient/', views.patient),
    path('update_patient/<int:pk>/', views.update_patient),
    path('delete_patient/<int:pk>/', views.delete_patient),
    path('add_nurse/', views.post_nurse),
    path('nurse/', views.nurse),
    path('update_nurse/<int:pk>/', views.update_nurse),
    path('delete_nurse/<int:pk>/', views.delete_nurse),
    path('add_staff/', views.post_staff),
    path('staff/', views.staff),
    path('update_staff/<int:pk>/', views.update_staff),
    path('delete_staff/<int:pk>/', views.delete_staff),
    
]