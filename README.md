# BoardingNest

BoardingNest is a web application built with Django that connects landlords with customers looking for boarding houses. The application features a beautiful pink-themed design and provides separate dashboards for landlords and customers.

## Features

### For Customers
- Browse available rooms (single and double types)
- Search and filter rooms by type
- View detailed room descriptions
- Contact landlords directly via phone, Facebook, Instagram, or other platforms
- View room images and pricing

### For Landlords
- Post available rooms with detailed descriptions
- Add contact information (phone, social media, etc.)
- Upload room images
- Edit existing room listings
- Delete room listings
- Mark rooms as available/unavailable

### User Roles
- **Admin**: Full access to Django admin panel
- **Landlord**: Can post, edit, and manage room listings
- **Customer**: Can view available rooms and contact landlords

## Installation

1. Install Python (3.8 or higher recommended)

2. Install Django and required packages:
```bash
pip install -r requirements.txt
```

3. Run migrations to create the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to:
```
http://localhost:8000/
```

## Usage

### Getting Started
1. Visit the welcome page at the root URL
2. Register for an account by choosing your role (Customer or Landlord)
3. If you choose Customer, you'll be able to browse available rooms
4. If you choose Landlord, you'll be able to post and manage room listings

### Creating Your First Room Post (For Landlords)
1. Login as a landlord
2. Click "Add New Room"
3. Fill in the room details:
   - Title
   - Room type (Single or Double)
   - Description
   - Price (optional)
   - Location
   - Contact information
   - Social media links
   - Upload a room image
4. Mark as available if the room is currently available
5. Click "Save Room"

### Searching for Rooms (For Customers)
1. Login as a customer
2. Use the search bar to search by title
3. Filter by room type (Single or Double)
4. Browse through the results
5. Contact landlords using the provided contact information

## Project Structure

```
boardingnest/
├── boardingnest/          # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── ...
├── core/                  # Main application
│   ├── models.py         # Database models (User, Room)
│   ├── views.py          # View functions
│   ├── forms.py          # Forms for registration and room posting
│   ├── urls.py           # App URL configuration
│   ├── admin.py          # Admin panel configuration
│   └── templates/        # HTML templates
│       └── core/         # Template files
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Technologies Used
- Django 4.2+
- Python 3.8+
- SQLite (default database)
- HTML5, CSS3 (Custom pink-themed styling)

## Theme
The application features a beautiful pink color scheme with:
- Gradient backgrounds
- Smooth animations and transitions
- Responsive design
- Modern UI/UX

## License
This project is created for educational and commercial use.

