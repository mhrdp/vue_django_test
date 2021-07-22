from django.conf import settings
from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import TokenRefreshView

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
    path('api/posts/<str:post_username>/<slug:post_slug>/', posts.GetDetailPostView.as_view()),

    path('api/referred/', posts.CreateReferredPostView.as_view()),
    path('api/referred/<str:username>/', posts.GetUserReferredPostView.as_view()),
    path('api/referred/<str:post_username>/<slug:post_slug>/referto/<slug:referred_post_slug>', posts.GetReferredPostView.as_view()),
    

    path('api/user/', users_api.CurrentUserView.as_view()),

    # REST Framework built-in login page for testing
    # Accessed by ../backdoor/rest/login or ../backdor/rest/logout
    path('rest/', include('rest_framework.urls')),
    path('token/', users_api.TokenPOSTMethod.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
