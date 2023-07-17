from django.test import TestCase
from django.contrib.auth.models import User
from .models import Doctor, Patient, Medicine, Prescription


class DoctorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the doctor
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a doctor
        cls.doctor = Doctor.objects.create(doctor_name='Dr. Smith', specialty='Cardiology', user=cls.user)

    def test_doctor_name_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('doctor_name').verbose_name
        self.assertEqual(field_label, 'doctor name')

    def test_specialty_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('specialty').verbose_name
        self.assertEqual(field_label, 'specialty')

    def test_user_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_doctor_name_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('doctor_name').max_length
        self.assertEqual(max_length, 100)

    def test_specialty_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('specialty').max_length
        self.assertEqual(max_length, 100)

    def test_user(self):
        doctor = Doctor.objects.get(id=1)
        user = doctor.user
        self.assertEqual(user, self.user)


class PatientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the patient
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a doctor for the patient
        cls.doctor = Doctor.objects.create(doctor_name='Dr. Smith', specialty='Cardiology', user=cls.user)

        # Create a patient
        cls.patient = Patient.objects.create(patient_name='John Doe', date_of_birth='1990-01-01', doctor=cls.doctor,
                                             user=cls.user)

    def test_patient_name_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('patient_name').verbose_name
        self.assertEqual(field_label, 'patient name')

    def test_date_of_birth_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_doctor_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('doctor').verbose_name
        self.assertEqual(field_label, 'doctor')

    def test_user_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_patient_name_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('patient_name').max_length
        self.assertEqual(max_length, 100)

    def test_date_of_birth(self):
        patient = Patient.objects.get(id=1)
        date_of_birth = patient.date_of_birth
        self.assertEqual(str(date_of_birth), '1990-01-01')

    def test_doctor(self):
        patient = Patient.objects.get(id=1)
        doctor = patient.doctor
        self.assertEqual(doctor, self.doctor)

    def test_user(self):
        patient = Patient.objects.get(id=1)
        user = patient.user
        self.assertEqual(user, self.user)


class MedicineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a medicine
        cls.medicine = Medicine.objects.create(medicine_name='Aspirin')

    def test_medicine_name_label(self):
        medicine = Medicine.objects.get(id=1)
        field_label = medicine._meta.get_field('medicine_name').verbose_name
        self.assertEqual(field_label, 'medicine name')

    def test_medicine_name_max_length(self):
        medicine = Medicine.objects.get(id=1)
        max_length = medicine._meta.get_field('medicine_name').max_length
        self.assertEqual(max_length, 100)


class PrescriptionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the doctor
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a doctor for the patient
        cls.doctor = Doctor.objects.create(doctor_name='Dr. Smith', specialty='Cardiology', user=cls.user)

        # Create a patient
        cls.patient = Patient.objects.create(patient_name='John Doe', date_of_birth='1990-01-01', doctor=cls.doctor,
                                             user=cls.user)

        # Create a medicine
        cls.medicine = Medicine.objects.create(medicine_name='Aspirin')

        # Create a prescription
        cls.prescription = Prescription.objects.create(patient=cls.patient, medicine=cls.medicine, dosage='10mg')

    def test_patient_label(self):
        prescription = Prescription.objects.get(id=1)
        field_label = prescription._meta.get_field('patient').verbose_name
        self.assertEqual(field_label, 'patient')

    def test_medicine_label(self):
        prescription = Prescription.objects.get(id=1)
        field_label = prescription._meta.get_field('medicine').verbose_name
        self.assertEqual(field_label, 'medicine')

    def test_dosage_label(self):
        prescription = Prescription.objects.get(id=1)
        field_label = prescription._meta.get_field('dosage').verbose_name
        self.assertEqual(field_label, 'dosage')

    def test_patient(self):
        prescription = Prescription.objects.get(id=1)
        patient = prescription.patient
        self.assertEqual(patient, self.patient)

    def test_medicine(self):
        prescription = Prescription.objects.get(id=1)
        medicine = prescription.medicine
        self.assertEqual(medicine, self.medicine)

    def test_dosage_max_length(self):
        prescription = Prescription.objects.get(id=1)
        max_length = prescription._meta.get_field('dosage').max_length
        self.assertEqual(max_length, 100)