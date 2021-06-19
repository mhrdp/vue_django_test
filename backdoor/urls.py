from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views

from .accounts import users_api

router = routers.DefaultRouter()
router.register('user_profile', users_api.UserProfileView)
router.register('is_premium', users_api.IsPremiumUser)


urlpatterns = [
    path('accounts/', include(router.urls)),

    # REST Framework built-in login page for testing
    # Accessed by ../backdoor/login or ../backdor/logout
    path('', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
]
