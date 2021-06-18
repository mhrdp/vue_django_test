from django.urls import path, include
from .accounts import views

urlpatterns = [
    path('users/', views.UserAPI.as_view()),
    path('users/premium/', views.PremiumUserAPI.as_view()),
    path('users/register/', views.UserRegisterAPI.as_view()),
    path('users/a/', views.premium_user_api),

    # REST Framework built-in login page for testing
    # Accessed by ../backdoor/login or ../backdor/logout
    path('', include('rest_framework.urls')),
]
