# Car Servicing System in Django

This Django-based car servicing system streamlines vehicle maintenance operations by automating service request management, mechanic assignments, and customer interactions. It provides a web interface for admins to approve or reject service requests, assign mechanics, estimate costs, and view feedback, while customers can submit service inquiries, check statuses, and update profiles. Built with Python, Django, and SQLite3, the system is ideal for vehicle service garages aiming to enhance efficiency and customer satisfaction.

## Features
- **Admin Dashboard**: Approve/reject customer service requests, assign mechanics, estimate service costs, and view customer/mechanic feedback.
- **Customer Portal**: Register, log in, submit service requests (with vehicle details and problem descriptions), check request status (Pending, Approved, Repairing, Done, Released), and view invoices.
- **Mechanic Management**: Admins can add, manage, and assign mechanics to service requests.
- **Feedback System**: Customers and mechanics can submit feedback, viewable by admins.
- **Profile Management**: Customers and mechanics can edit profiles (requires re-login after updates due to session handling).
- **Theme Switching**: Toggle between light and dark themes for the web interface.
- **Automated Deletion**: If a customer is deleted, their service requests are automatically removed.

## Hardware Requirements
- A computer with internet access for development and hosting.
- (Optional) A server or local machine to deploy the Django application (e.g., using Gunicorn and Nginx).

## Software Requirements
- **Python 3.7+** (recommended: 3.7.6, as in)[](https://github.com/sumitkumar1503/vehicleservicemanagement)
- **Django 3.0.5** (or compatible version)
- **Libraries**:
  - `django` (install via `pip install django==3.0.5`)
  - `django-widget-tweaks` (install via `pip install django-widget-tweaks`)
- **SQLite3** (included with Python; no separate installation needed)
- **Web Browser** for accessing the application
- **(Optional)** Email service for notifications (e.g., Gmail SMTP, configured in `settings.py`)

## Setup Instructions
1. **Install Prerequisites**:
   - Install Python 3.7+ (ensure "Add to Path" is checked during installation).
   - Open a terminal and install required packages:
     ```bash
     pip install django==3.0.5 django-widget-tweaks
     ```

2. **Download and Setup Project**:
   - Clone or download the repository:
     ```bash
     git clone https://github.com/your-username/CarServicingDjango.git
     ```
   - Navigate to the project folder:
     ```bash
     cd CarServicingDjango
     ```

3. **Configure the Database**:
   - Run migrations to set up the SQLite3 database:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4. **(Optional) Configure Email Notifications**:
   - Update `settings.py` with your email settings (e.g., Gmail SMTP):
     ```python
     EMAIL_HOST = 'smtp.gmail.com'
     EMAIL_PORT = 587
     EMAIL_HOST_USER = 'youremail@gmail.com'
     EMAIL_HOST_PASSWORD = 'your-email-password'
     EMAIL_USE_TLS = True
     ```
   - Log in to your Gmail account, enable "Less secure app access" or use an App Password (see Google Account settings).

5. **Run the Application**:
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```
   - Open a browser and navigate to `http://127.0.0.1:8000`.

6. **Create Admin Account**:
   - Create a superuser to access the admin dashboard:
     ```bash
     python manage.py createsuperuser
     ```
   - Log in at `http://127.0.0.1:8000/admin`.

## Usage
- **Admins**: Log in to the admin dashboard to manage service requests, assign mechanics, estimate costs, and view feedback.
- **Customers**: Register, submit service requests with vehicle details (e.g., number, model, problem), check status, and view invoices.
- **Mechanics**: View assigned tasks and submit feedback (if implemented).
- **Note**: Profile updates require re-login due to session updates in the database.

## Project Structure
