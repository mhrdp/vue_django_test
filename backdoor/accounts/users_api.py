from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from django.views.generic import View

from .models import RegisteredUser, Profile, PremiumUser
from .serializers import UserSerializer, ProfileSerializer, PremiumUserSerializer

# Get all user profiles, admin only
class UserView(ModelViewSet):
    permission_classes = [AllowAny]
    View.http_method_names = ['post']
    
    # disable web browsable API
    renderer_classes = [JSONRenderer]
    
    queryset = RegisteredUser.objects.all()
    serializer_class = UserSerializer

class UserProfileView(ModelViewSet):
    authentication_classes = [
        SessionAuthentication, BasicAuthentication
        ]
    permission_classes = [IsAdminUser]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Get all user VIP status, admin only
class IsPremiumUser(ModelViewSet):
    authentication_classes = [
        SessionAuthentication, BasicAuthentication
        ]
    permission_classes = [IsAdminUser]

    queryset = PremiumUser.objects.all()
    serializer_class = PremiumUserSerializer