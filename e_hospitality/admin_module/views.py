from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Facility, Department
from .forms import FacilityForm, DepartmentForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    facilities = Facility.objects.all()
    departments = Department.objects.all()
    return render(request, 'admin_module/dashboard.html', {
        'facilities': facilities,
        'departments': departments
    })

@user_passes_test(is_admin)
def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FacilityForm()
    return render(request, 'admin_module/add_facility.html', {'form': form})

@user_passes_test(is_admin)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = DepartmentForm()
    return render(request, 'admin_module/add_department.html', {'form': form})