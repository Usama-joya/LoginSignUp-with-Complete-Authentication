
from django.urls import path
from loginsiginupApp.views import UserRegistrationView,LoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('RestPasswordView/<uid>/<token>/', UserPasswordResetView.as_view(),name='RestPasswordView'),
]