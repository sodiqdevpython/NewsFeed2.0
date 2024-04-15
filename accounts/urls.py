from django.urls import path
from .views import login_view, logout_view, profile, password_change_view, register_view, update_profile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
    PasswordResetCompleteView

urlpatterns = [
    path('signup/', register_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('password_change/', password_change_view, name='password_change'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]