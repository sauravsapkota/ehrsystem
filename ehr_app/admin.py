from django.contrib import admin
from .models import Doctor, Patient, Medicine, Prescription

# Register your models here.
admin.site.register([Doctor, Patient, Medicine, Prescription])

