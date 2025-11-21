from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('landlord-dashboard/', views.landlord_dashboard, name='landlord_dashboard'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('profile/', views.profile_view, name='profile'),
    path('request-availability/<int:room_id>/', views.request_availability, name='request_availability'),
    path('landlord-notifications/', views.landlord_notifications, name='landlord_notifications'),
    path('customer-requests/', views.customer_requests, name='customer_requests'),
    path('update-request-status/<int:request_id>/', views.update_request_status, name='update_request_status'),
    path('landlord-history/', views.landlord_history, name='landlord_history'),
    path('customer-history/', views.customer_history, name='customer_history'),
    path('logo/', views.logo_view, name='logo'),
    path('poster/', views.poster_view, name='poster'),
    path('video/', views.video_view, name='video'),
    path('search/', views.public_search, name='public_search'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

