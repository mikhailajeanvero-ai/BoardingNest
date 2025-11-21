from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, RoomForm, ProfileUpdateForm
from .models import Room, AvailabilityRequest, Notification, RequestHistory


def welcome(request):
    return render(request, 'core/welcome.html')


def register_view(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account successfully created, {user.username}! Welcome to BoardingNest!')
            if user.role == 'landlord':
                return redirect('landlord_dashboard')
            elif user.role == 'administrator':
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return redirect('admin_dashboard')
            else:
                return redirect('customer_dashboard')
    
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.role == 'landlord':
                return redirect('landlord_dashboard')
            else:
                return redirect('customer_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('welcome')


@login_required
def customer_dashboard(request):
    if request.user.role != 'customer':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    rooms = Room.objects.filter(is_available=True)
    query = request.GET.get('search')
    room_type = request.GET.get('room_type')
    
    if query:
        rooms = rooms.filter(title__icontains=query)
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    
    context = {
        'rooms': rooms,
        'search_query': query,
        'room_type_filter': room_type,
    }
    return render(request, 'core/customer_dashboard.html', context)


@login_required
def landlord_dashboard(request):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    rooms = Room.objects.filter(landlord=request.user)
    context = {
        'rooms': rooms,
    }
    return render(request, 'core/landlord_dashboard.html', context)


@login_required
def add_room(request):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.landlord = request.user
            room.save()
            messages.success(request, 'Room added successfully!')
            return redirect('landlord_dashboard')
    else:
        form = RoomForm()
    
    return render(request, 'core/add_room.html', {'form': form})


@login_required
def edit_room(request, room_id):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    room = get_object_or_404(Room, id=room_id, landlord=request.user)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully!')
            return redirect('landlord_dashboard')
    else:
        form = RoomForm(instance=room)
    
    return render(request, 'core/edit_room.html', {'form': form, 'room': room})


@login_required
def delete_room(request, room_id):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    room = get_object_or_404(Room, id=room_id, landlord=request.user)
    
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully!')
        return redirect('landlord_dashboard')
    
    return render(request, 'core/delete_room.html', {'room': room})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'core/profile.html', {'form': form})


@login_required
def request_availability(request, room_id):
    if request.user.role != 'customer':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        existing_request = AvailabilityRequest.objects.filter(
            room=room, 
            customer=request.user, 
            status='pending'
        ).exists()
        
        if existing_request:
            messages.info(request, 'You have already requested availability for this room.')
        else:
            availability_request = AvailabilityRequest.objects.create(
                room=room,
                customer=request.user,
                message=f"Customer {request.user.get_full_name() or request.user.username} is interested in this room."
            )
            
            # Create notification for the landlord
            Notification.objects.create(
                user=room.landlord,
                availability_request=availability_request,
                message=f"{request.user.get_full_name() or request.user.username} requested availability for your room: {room.title}"
            )
            
            # Create notification for the customer
            Notification.objects.create(
                user=request.user,
                availability_request=availability_request,
                message=f"You requested room availability for '{room.title}' posted by {room.landlord.get_full_name() or room.landlord.username}"
            )
            
            messages.success(request, 'Availability request sent successfully! The landlord has been notified.')
    
    return redirect('customer_dashboard')


@login_required
def landlord_notifications(request):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    # Get requests for rooms owned by this landlord
    requests = AvailabilityRequest.objects.filter(
        room__landlord=request.user
    ).select_related('customer', 'room')
    
    pending_count = requests.filter(status='pending').count()
    
    # Mark notifications as read when landlord reviews requests
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    
    context = {
        'requests': requests,
        'pending_count': pending_count,
    }
    return render(request, 'core/landlord_notifications.html', context)


@login_required
def update_request_status(request, request_id):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    avail_request = get_object_or_404(
        AvailabilityRequest, 
        id=request_id, 
        room__landlord=request.user
    )
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['approved', 'rejected']:
            avail_request.status = status
            avail_request.save()
            
            # Mark room as unavailable if approved
            if status == 'approved':
                avail_request.room.is_available = False
                avail_request.room.save()
            
            # Create history for landlord
            action = 'Accepted' if status == 'approved' else 'Declined'
            RequestHistory.objects.create(
                availability_request=avail_request,
                user=request.user,
                action=action,
                message=f"{action} request from {avail_request.customer.get_full_name() or avail_request.customer.username} for room '{avail_request.room.title}'"
            )
            
            # Create history for customer
            RequestHistory.objects.create(
                availability_request=avail_request,
                user=avail_request.customer,
                action=f'Request {action}',
                message=f"Your request for room '{avail_request.room.title}' was {action.lower()} by {request.user.get_full_name() or request.user.username}"
            )
            
            # Delete related notifications
            Notification.objects.filter(availability_request=avail_request).delete()
            
            status_message = 'approved' if status == 'approved' else 'declined'
            messages.success(request, f'Request {status_message} successfully!')
        else:
            messages.error(request, 'Invalid status value.')
    
    return redirect('landlord_notifications')


@login_required
def customer_requests(request):
    if request.user.role != 'customer':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    # Get all requests made by this customer
    requests = AvailabilityRequest.objects.filter(
        customer=request.user
    ).select_related('room', 'room__landlord')
    
    # Mark notifications as read when customer reviews their requests
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    
    context = {
        'requests': requests,
    }
    return render(request, 'core/customer_requests.html', context)


@login_required
def landlord_history(request):
    if request.user.role != 'landlord':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    history = RequestHistory.objects.filter(user=request.user).select_related('availability_request__room', 'availability_request__customer')
    
    context = {
        'history': history,
    }
    return render(request, 'core/landlord_history.html', context)


@login_required
def customer_history(request):
    if request.user.role != 'customer':
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    history = RequestHistory.objects.filter(user=request.user).select_related('availability_request__room', 'availability_request__room__landlord')
    
    context = {
        'history': history,
    }
    return render(request, 'core/customer_history.html', context)


@login_required
def logo_view(request):
    return render(request, 'core/logo.html')


@login_required
def poster_view(request):
    return render(request, 'core/poster.html')


@login_required
def video_view(request):
    return render(request, 'core/video.html')


def public_search(request):
    from django.db.models import Q
    
    rooms = Room.objects.filter(is_available=True)
    query = request.GET.get('search')
    room_type = request.GET.get('room_type')
    
    if query:
        rooms = rooms.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(landlord__username__icontains=query) |
            Q(landlord__first_name__icontains=query) |
            Q(landlord__last_name__icontains=query)
        )
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    
    context = {
        'rooms': rooms,
        'search_query': query,
        'room_type_filter': room_type,
    }
    return render(request, 'core/public_search.html', context)


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    from .models import User
    from django.db.models import Q
    
    users = User.objects.filter(role__in=['customer', 'landlord']).order_by('-date_joined')
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(username__icontains=search_query)
        )
    
    context = {
        'users': users,
        'search_query': search_query,
    }
    return render(request, 'core/admin_dashboard.html', context)


@login_required
def home(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    elif request.user.role == 'landlord':
        return redirect('landlord_dashboard')
    else:
        return redirect('customer_dashboard')
