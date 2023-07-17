# Electronic Health Record (EHR) System API

This project is a Django-based API that provides endpoints for an Electronic Health Record (EHR) system. It allows you to manage doctors, patients, medicines, and prescriptions.

## Instructions to Run

1. Clone the repository or download the code files.

2. Install the required dependencies. Make sure you have Python, Django and Django Rest Framework installed. You can install the dependencies using pip:
```
pip install django djangorestframework
```

3. Install the required dependencies. Run the following command:
```
pip install -r requirements.txt
```
4. Set up the database. Open the `ehr_project/settings.py` file and configure the database settings according to your environment.

5. Apply the database migrations. Run the following command:
```
python manage.py migrate
```
6. Start the Django development server. Run the following command:
```
python manage.py runserver
```

7. Access the API endpoints in your web browser or using an API client such as Postman:

- Doctors: [http://localhost:8000/doctors/](http://localhost:8000/doctors/)
- Patients: [http://localhost:8000/patients/](http://localhost:8000/patients/)
- Medicines: [http://localhost:8000/medicines/](http://localhost:8000/medicines/)
- Prescriptions: [http://localhost:8000/prescriptions/](http://localhost:8000/prescriptions/)

## Technologies Used

- Django
- Django Rest Framework
- Python

## API Endpoints

The API provides the following endpoints:

- `/doctors/`: GET all doctors
- `/patients/`: GET all patients
- `/medicines/`: GET all medicines
- `/prescriptions/`: GET all prescriptions

Each endpoint supports the standard HTTP methods (GET, POST, PUT, DELETE) for CRUD operations.

## Database Schema

The database schema for this EHR system includes the following tables:

- `Doctor`: Stores information about doctors, including their name and specialty.
- `Patient`: Stores information about patients, including their name, date of birth, and the assigned doctor.
- `Medicine`: Stores information about prescribed medicines.
- `Prescription`: Links patients with prescribed medicines, storing the dosage information.

Please refer to the schema section in the project for a detailed representation of the database schema.

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/)

## License

This project is licensed under the [MIT License](LICENSE).

## Troubleshooting

If you encounter any issues while setting up or running the EHR system, refer to the documentation or contact the system administrator or developer for assistance.
