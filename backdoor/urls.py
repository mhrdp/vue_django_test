from django.conf import settings
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from .accounts import users_api

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouters()

router.register('user_profile', users_api.UserProfileView)
router.register('is_premium', users_api.IsPremiumUser)
router.register('users', users_api.UserView)


urlpatterns = [
    path('accounts/', include(router.urls)),

    # REST Framework built-in login page for testing
    # Accessed by ../backdoor/rest/login or ../backdor/rest/logout
    path('rest/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
