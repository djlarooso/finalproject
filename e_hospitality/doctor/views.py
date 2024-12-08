from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Prescription
from patient.models import Appointment, MedicalRecord
from .forms import PrescriptionForm


@login_required
def doctor_dashboard(request):
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor/dashboard.html', {
        'doctor': doctor,
        'appointments': appointments
    })


@login_required
def patient_details(request, patient_id):
    doctor = request.user.doctor
    patient = Patient.objects.get(id=patient_id)
    medical_records = MedicalRecord.objects.filter(patient=patient)
    prescriptions = Prescription.objects.filter(doctor=doctor, patient=patient)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = doctor
            prescription.patient = patient
            prescription.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = PrescriptionForm()

    return render(request, 'doctor/patient_details.html', {
        'patient': patient,
        'medical_records': medical_records,
        'prescriptions': prescriptions,
        'form': form
    })