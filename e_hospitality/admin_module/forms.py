from django import forms
from .models import Facility, Department

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'address', 'phone_number']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'facility']