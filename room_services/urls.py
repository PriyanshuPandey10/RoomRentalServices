"""room_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('contact_us',contact_us,name='contact_us'),
    path('admin_home',admin_home,name='admin_home'),
    path('logout',logout,name='logout'),
    path('user_home',user_home,name='user_home'),
    path('add_room',add_room,name='add_room'),
    path('view_room_admin',view_room_admin,name='view_room_admin'),
    path('delete_room/<int:id>',delete_room,name='delete_room'),
    path('edit_room/<int:pid>',edit_room,name='edit_room'),
    path('view_booking_admin',view_booking_admin,name='view_booking_admin'),
    path('view_room_user',view_room_user,name='view_room_user'),
    path('change_password_user',change_password_user,name='change_password_user'),
    path('change_password_admin',change_password_admin,name='change_password_admin'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('user_booking',user_booking,name='user_booking'),
    path('book_room/<int:id>',book_room,name='book_room'),
    path('change_status/<int:id>',change_status,name='change_status'),
    path('view_user',view_user,name='view_user'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('delete_booking/<int:id>',delete_booking,name='delete_booking'),
    path('cancel_booking/<int:id>',cancel_booking,name='cancel_booking'),
    path('view_contact',view_contact,name='view_contact'),
    path('delete_contact/<int:id>',delete_contact,name='delete_contact'),
    path('search',search,name='search'),
    path('searchh',searchh,name='searchh'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
