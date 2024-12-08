from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patient_registration, name='patient_registration'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('bills/', views.patient_bills, name='patient_bills'),
]