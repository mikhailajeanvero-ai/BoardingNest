# 🪶 BoardingNest - Start Here!

## Quick Setup (3 Simple Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Server
```bash
python manage.py runserver
```
Or simply double-click `run.bat` on Windows!

### Step 3: Open in Browser
Go to: **http://localhost:8000/**

---

## ✨ What's Implemented

### ✅ Registration & Login
- Sign up creates account in database ✓
- Automatic login after sign up ✓
- Success message: "Account successfully created, [username]!" ✓
- Redirects to appropriate dashboard ✓
- Login shows: "Welcome back, [username]!" ✓

### ✅ User Features

**Customer:**
- View all available rooms on homepage
- See complete address (highlighted in pink box)
- See landlord contact number (highlighted in blue box)
- See bed type: 🛏️ Single Bed or 🛏️ Double Bed
- Search rooms by title
- Filter by room type
- Contact landlords via phone, Facebook, Instagram

**Landlord:**
- Post rooms with all details
- Add complete address
- Add contact information
- Upload room images
- Edit existing rooms
- Delete rooms
- Mark availability status

### ✅ Pink Theme
- Beautiful pink gradients throughout
- Pink navigation bar
- Pink buttons and accents
- Smooth animations

---

## 🎯 Try It Now!

1. **First Time Use:**
   - Click "Sign Up"
   - Choose "Customer" or "Landlord"
   - Fill in details
   - Click "Create Account"
   - See success message!
   - Automatically logged in and redirected!

2. **Login:**
   - Use your credentials
   - See "Welcome back, [your name]!"
   - Go to your dashboard

3. **View Rooms:**
   - Address displayed in pink box
   - Contact displayed in blue box
   - Bed type clearly shown
   - All information prominent!

---

## 📁 Project Files

- `boardingnest/` - Django project settings
- `core/` - Main application
- `core/models.py` - Database models (User, Room)
- `core/templates/core/` - All HTML templates
- `core/views.py` - Business logic
- `db.sqlite3` - Database file
- `media/` - Images uploaded by landlords

---

## 🚀 Need Help?

- See `INSTRUCTIONS.md` for detailed guide
- See `SETUP.md` for setup instructions
- See `README.md` for full documentation

---

## 🎉 Ready to Go!

Everything is set up and ready to use. Just run the server and start creating accounts!

Happy boarding hunting! 🏠

