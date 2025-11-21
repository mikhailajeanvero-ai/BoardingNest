from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('landlord', 'Landlord'),
        ('administrator', 'Administrator'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=20, blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    other_contact = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
    ]
    
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    title = models.CharField(max_length=200)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    other_contact = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.get_room_type_display()}"
    
    class Meta:
        ordering = ['-created_at']


class AvailabilityRequest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='availability_requests')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availability_requests')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.username} - {self.room.title} - {self.get_status_display()}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Availability Request'
        verbose_name_plural = 'Availability Requests'

class Notification(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notifications')
    availability_request = models.ForeignKey('AvailabilityRequest', on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class RequestHistory(models.Model):
    availability_request = models.ForeignKey(AvailabilityRequest, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_history')
    action = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Request History'
        verbose_name_plural = 'Request Histories'
