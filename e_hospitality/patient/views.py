from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, MedicalRecord, Bill
from .forms import PatientRegistrationForm, AppointmentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from doctor.models import Doctor
from django.contrib.auth import login

def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Patient.objects.create(
                user=user,
                date_of_birth=form.cleaned_data['date_of_birth'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')  # Using the correct URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/registration.html', {'form': form})


@login_required
def patient_dashboard(request):
    if not hasattr(request.user, 'patient'):
        messages.error(request, 'Please complete your patient registration first.')
        return redirect('patient_registration')

    patient = request.user.patient
    appointments = Appointment.objects.filter(patient=patient).order_by('date_time')
    medical_records = MedicalRecord.objects.filter(patient=patient).order_by('-date')
    bills = Bill.objects.filter(patient=patient).order_by('-date')

    return render(request, 'patient/dashboard.html', {
        'patient': patient,
        'appointments': appointments,
        'medical_records': medical_records,
        'bills': bills
    })

@login_required
def book_appointment(request):
    doctors = Doctor.objects.all().select_related('user')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('patient_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    return render(request, 'patient/book_appointment.html', {
        'form': form,
        'doctors': doctors
    })

@login_required
def patient_bills(request):
    patient = request.user.patient
    bills = Bill.objects.filter(patient=patient).order_by('-date')
    return render(request, 'patient/bills.html', {'bills': bills})