from django.contrib import admin
from .models import User, Room, AvailabilityRequest, Notification, RequestHistory


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'phone_number']
    list_filter = ['role']
    search_fields = ['username', 'email']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'room_type', 'landlord', 'is_available', 'created_at']
    list_filter = ['room_type', 'is_available', 'created_at']
    search_fields = ['title', 'description', 'landlord__username']


@admin.register(AvailabilityRequest)
class AvailabilityRequestAdmin(admin.ModelAdmin):
    list_display = ['customer', 'room', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer__username', 'room__title']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'message']


@admin.register(RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['user__username', 'message', 'action']

