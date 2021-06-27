from django.conf import settings
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from .accounts import users_api
from .posts import posts

# Router for Viewset Class Based
if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouters()

# Viewset GET
router.register('user-profile', users_api.GetProfileView)
router.register('is-premium', users_api.IsPremiumUser)

# Viewset POST
router.register('users', users_api.CreateUserView)


urlpatterns = [
    path('api/', include(router.urls)),
    
    path('api/posts/', posts.CreatePostView.as_view()),
    path('api/posts/<str:username>/', posts.GetUserPostView.as_view()),

    # REST Framework built-in login page for testing
    # Accessed by ../backdoor/rest/login or ../backdor/rest/logout
    path('rest/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
