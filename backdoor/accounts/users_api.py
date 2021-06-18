from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Profile, PremiumUser
from .serializers import ProfileSerializer, PremiumUserSerializer

# Get all user profiles, admin only
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