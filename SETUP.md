# BoardingNest Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Database
The database has already been created, but if you need to recreate it:
```bash
python manage.py migrate
```

### 3. Create Admin Account (Optional)
To create a superuser/admin account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin account.

### 4. Run the Server
```bash
python manage.py runserver
```
Or simply double-click `run.bat` on Windows.

### 5. Access the Application
Open your browser and go to:
```
http://localhost:8000/
```

## Creating Test Accounts

### Method 1: Using the Web Interface
1. Go to the welcome page
2. Click "Sign Up"
3. Choose your role:
   - **Customer**: If you want to browse available rooms
   - **Landlord**: If you want to post room listings

### Method 2: Using Django Admin
1. Create a superuser account (see step 3 above)
2. Go to http://localhost:8000/admin/
3. Login with your admin credentials
4. Navigate to Users to create or manage user accounts

## Default Admin URL
```
http://localhost:8000/admin/
```

## User Roles

### Admin
- Full access to Django admin panel
- Can manage all users and rooms
- Access: http://localhost:8000/admin/

### Landlord
- Post new room listings
- Edit existing room listings
- Delete room listings
- Manage contact information
- Access: http://localhost:8000/landlord-dashboard/

### Customer
- Browse available rooms
- Search and filter rooms
- View room details
- Contact landlords
- Access: http://localhost:8000/customer-dashboard/

## Project Structure
- `core/` - Main application directory
- `core/models.py` - Database models (User, Room)
- `core/views.py` - View functions
- `core/templates/` - HTML templates
- `boardingnest/` - Django project settings
- `manage.py` - Django management script

## Troubleshooting

### Database errors
If you encounter database errors, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static files not loading
Create the static files directory:
```bash
python manage.py collectstatic
```

### Image upload errors
Make sure the `media` folder exists in the project root.

## Features to Test

1. **Welcome Page**: Landing page with login/register options
2. **Registration**: Create customer or landlord accounts
3. **Login**: Access different dashboards based on user role
4. **Customer Dashboard**: Browse and search available rooms
5. **Landlord Dashboard**: Manage room listings
6. **Add Room**: Create new room posts with images
7. **Edit Room**: Update existing room information
8. **Delete Room**: Remove room listings
9. **Search & Filter**: Find rooms by type and keywords

## Support
For issues or questions, please refer to the main README.md file.

