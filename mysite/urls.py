from django.contrib import admin
from django.urls import path, include
from account.views import (
    register_view as account_register,
    login_view,
    logout_view

) 
from django.contrib.auth import views as auth_views
from magazine.views import email_list_signup
from GISapp.views import get_drawings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdrawings/',get_drawings,name ='getdrawings'),
    path('', include('articles.urls', namespace='articles')),
    path('contactus/',include('contactus.urls',namespace='contactus')),
     path('',include('GISapp.urls',namespace='GISapp')),
    path('register/',account_register,name='register'),
    path('login/',login_view, name="login"),
    path('logout/',logout_view,name='logout'),
        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),

    path('subscribe/',email_list_signup,name="subscribe"),
    path('menus/',include("menus.urls",namespace='menus')),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    
]
