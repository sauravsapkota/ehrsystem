"""
URL configuration for ehrsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ehr_app.views import DoctorList, PatientList, MedicineList, PrescriptionList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', DoctorList.as_view(), name='doctor_list'),
    path('patients/', PatientList.as_view(), name='patient_list'),
    path('medicines/', MedicineList.as_view(), name='medicine_list'),
    path('prescriptions/', PrescriptionList.as_view(), name='prescription_list'),
]
