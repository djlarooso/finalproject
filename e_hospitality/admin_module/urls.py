from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-facility/', views.add_facility, name='add_facility'),
    path('add-department/', views.add_department, name='add_department'),
]