from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)