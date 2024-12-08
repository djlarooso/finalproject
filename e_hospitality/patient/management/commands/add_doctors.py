from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from doctor.models import Doctor

class Command(BaseCommand):
    help = 'Add initial doctors to the database'

    def handle(self, *args, **kwargs):
        # List of doctors with their details
        doctors_data = [
            {
                'username': 'dr.smith',
                'first_name': 'John',
                'last_name': 'Smith',
                'email': 'dr.smith@hospital.com',
                'specialization': 'Cardiology',
                'license_number': 'CAR123456'
            },
            {
                'username': 'dr.patel',
                'first_name': 'Priya',
                'last_name': 'Patel',
                'email': 'dr.patel@hospital.com',
                'specialization': 'Pediatrics',
                'license_number': 'PED789012'
            },
            {
                'username': 'dr.wilson',
                'first_name': 'Sarah',
                'last_name': 'Wilson',
                'email': 'dr.wilson@hospital.com',
                'specialization': 'Orthopedics',
                'license_number': 'ORT345678'
            },
            {
                'username': 'dr.chen',
                'first_name': 'Michael',
                'last_name': 'Chen',
                'email': 'dr.chen@hospital.com',
                'specialization': 'Neurology',
                'license_number': 'NEU901234'
            },
            {
                'username': 'dr.rodriguez',
                'first_name': 'Maria',
                'last_name': 'Rodriguez',
                'email': 'dr.rodriguez@hospital.com',
                'specialization': 'Dermatology',
                'license_number': 'DER567890'
            }
        ]

        for doctor_data in doctors_data:
            try:
                # Create user account for doctor
                user = User.objects.create_user(
                    username=doctor_data['username'],
                    email=doctor_data['email'],
                    password='doctor123'  # Default password, should be changed
                )
                user.first_name = doctor_data['first_name']
                user.last_name = doctor_data['last_name']
                user.save()

                # Create doctor profile
                Doctor.objects.create(
                    user=user,
                    specialization=doctor_data['specialization'],
                    license_number=doctor_data['license_number']
                )

                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created doctor: Dr. {doctor_data["first_name"]} {doctor_data["last_name"]} - {doctor_data["specialization"]}'
                ))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'Failed to create doctor {doctor_data["username"]}: {str(e)}'
                ))