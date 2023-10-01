from django.urls import path
from . import views
from .forms import ForgotPasswordForm, NewPasswordForm

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path("", views.login, name="login"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("update_existing_profile/", views.update_existing_profile, name="update_existing_profile"),
    path("register/", views.register, name="register"),
    path("activate/<str:uidb64>/<str:token>/", views.activate, name="activate"),
    path("logout/", views.logout, name="logout"),
    
    path('password-reset/', PasswordResetView.as_view(template_name='user_accounts/password_reset.html',html_email_template_name='user_accounts/password_reset_email.html', form_class=ForgotPasswordForm),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user_accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user_accounts/password_reset_confirm.html',  form_class=NewPasswordForm) ,name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='user_accounts/password_reset_complete.html'),name='password_reset_complete'),
    
    
]
