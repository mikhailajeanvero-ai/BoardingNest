# BoardingNest - Quick Start Instructions

## ✅ All Requirements Implemented

### 🔐 Authentication System
- ✅ Sign up page with role selection (Customer/Landlord)
- ✅ Login page
- ✅ User information saved to database
- ✅ Automatic login after successful registration
- ✅ Welcome message with username displayed after login
- ✅ Success popup when account is created

### 🏠 User Roles

#### 1. **Customer** (Looking for rooms)
- Can view all available rooms
- Can search rooms by title
- Can filter by room type (Single/Double)
- Can see complete address
- Can see landlord contact number
- Can see type of bed (Single/Double)
- Can contact landlords via Facebook, Instagram, or phone

#### 2. **Landlord/Landlady** (Posting rooms)
- Can post available rooms with:
  - Room title
  - Room type (Single/Double)
  - Description
  - Price
  - Complete address
  - Contact information
  - Facebook/Instagram links
  - Room images
- Can edit existing room posts
- Can delete room posts
- Can mark rooms as available/unavailable

#### 3. **Admin**
- Full access to Django admin panel
- Can manage all users and rooms

### 🎨 Pink Theme
- ✅ Beautiful pink gradient backgrounds
- ✅ Pink-themed navigation bar
- ✅ Consistent pink color scheme throughout
- ✅ Smooth animations and transitions

## 🚀 How to Run

1. **Start the Server**
   ```bash
   python manage.py runserver
   ```
   Or double-click `run.bat`

2. **Open Your Browser**
   Go to: http://localhost:8000/

3. **Create Your First Account**
   - Click "Sign Up"
   - Choose your role (Customer or Landlord)
   - Fill in your information
   - Click "Create Account"
   - You'll see a success message and be automatically logged in!

4. **Create Admin Account** (Optional)
   ```bash
   python manage.py createsuperuser
   ```
   Or double-click `create_admin.bat`

## 📱 Features

### After Sign Up
- ✅ "Account successfully created, [username]! Welcome to BoardingNest!" message appears
- ✅ User is automatically logged in
- ✅ User is redirected to their dashboard based on role

### After Login
- ✅ "Welcome back, [username]!" message appears
- ✅ User is redirected to their appropriate dashboard

### Homepage (Customer Dashboard)
- ✅ Shows all available rooms
- ✅ Displays complete address in highlighted box
- ✅ Displays landlord contact number in highlighted box
- ✅ Shows room type (Single/Double bed) clearly
- ✅ Shows price, description, and social media links

## 📋 Example Registration Flow

1. Go to homepage → Click "Sign Up"
2. Enter:
   - Username: `john_customer`
   - Email: `john@example.com`
   - Role: `Customer (Looking for a room)`
   - Password: `yourpassword`
3. Click "Create Account"
4. Success message appears: "Account successfully created, john_customer! Welcome to BoardingNest!"
5. Automatically redirected to Customer Dashboard
6. Can now browse available rooms

## 🎯 Testing the System

### Test Customer Flow
1. Register as Customer
2. Login (or automatically logged in)
3. Browse available rooms on homepage
4. See room details, address, contact info, and bed type
5. Search for rooms
6. Filter by room type

### Test Landlord Flow
1. Register as Landlord
2. Click "Add New Room"
3. Fill in room details:
   - Title: "Cozy Single Room Near Campus"
   - Type: Single
   - Description: "Beautiful room with..."
   - Location: "123 Main St, City, Province"
   - Contact: "+63 912 345 6789"
   - Add Facebook/Instagram links
   - Upload image
4. Save room
5. Room appears on your dashboard
6. Edit or delete room as needed

## 💡 Tips

- All user accounts are stored in the database
- Login credentials work immediately after registration
- Address and contact info are prominently displayed
- Bed type is clearly visible with emoji (🛏️)
- Success messages appear at the top of the page
- Images are stored in the `media` folder

## 🎨 Color Scheme
- Primary Pink: `#FF1493` (Deep Pink)
- Secondary Pink: `#FF69B4` (Hot Pink)
- Light Pink: `#FFB6C1` (Light Pink)
- Background Gradient: Light pink to hot pink

Enjoy using BoardingNest! 🪶

