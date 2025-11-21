from .models import Notification, AvailabilityRequest


def notifications(request):
    """Add notifications and request counts to context"""
    context = {
        'unread_notifications': [],
        'notification_count': 0,
        'pending_requests_count': 0,
        'customer_pending_requests_count': 0,
    }
    
    user = getattr(request, 'user', None)
    if user and user.is_authenticated:
        # For landlords, get pending requests count
        if getattr(user, 'role', None) == 'landlord':
            context['pending_requests_count'] = AvailabilityRequest.objects.filter(
                room__landlord=user,
                status='pending'
            ).count()
        elif getattr(user, 'role', None) == 'customer':
            context['customer_pending_requests_count'] = AvailabilityRequest.objects.filter(
                customer=user,
                status='pending'
            ).count()
        
        # Get unread notifications for all users
        unread_notifications = Notification.objects.filter(
            user=user, 
            is_read=False
        ).order_by('-created_at')
        
        context['unread_notifications'] = list(unread_notifications[:3])
        context['notification_count'] = unread_notifications.count()
    
    return context

