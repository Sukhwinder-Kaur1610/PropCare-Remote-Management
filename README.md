# PropCare – Django Starter Project

A runnable Django MVP scaffold based on the PropCare Website & System Blueprint.

## 1. Requirements
- Python 3.10+
- pip

## 2. Setup (Windows PowerShell)
```powershell
cd PropCare_Django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

## 3. Included in this starter
- Registration, login and logout using Django authentication
- User profiles and roles (owner, manager, service provider, admin)
- Property CRUD with image upload
- Property ownership/identity verification submission records
- Inspection requests and reports
- Maintenance requests and status tracking
- Service catalogue
- Rental and sale listings
- Property expenses
- Notifications and owner-manager messages
- Role-aware dashboard entry points
- Django admin registrations for project data

## 4. Important implementation notes
- This is an educational MVP foundation, not a production-ready property/legal verification service.
- Uploaded ownership documents are stored in `media/` during local development. Do not expose sensitive documents publicly in production.
- The starter records verification submissions; it does not establish legal ownership or connect to government land records.
- Payment processing, email/SMS delivery, maps, AI/OCR, and production-grade authorization are extension tasks.
- For production, configure PostgreSQL, environment variables, HTTPS, private object storage, audit logging, backups, and stronger object-level permissions.

## 5. Create your first test account
Register through `/accounts/register/`. Choose a role. Then add a property from the dashboard.
