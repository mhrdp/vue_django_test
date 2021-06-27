from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)

from rest_framework.permissions import (
    IsAdminUser, AllowAny
)

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import RegisteredUser, Profile, PremiumUser
from .serializers import UserSerializer, ProfileSerializer, PremiumUserSerializer

# A VIEW TO DO ONLY CREATE AND UPDATE TO USER'S MODEL
class CreateUserView(ModelViewSet):
    permission_classes = [AllowAny]
    View.http_method_names = ['post', 'put']
    
    # disable web browsable API
    renderer_classes = [JSONRenderer]
    
    queryset = RegisteredUser.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response('Success')
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
            
class GetProfileView(ModelViewSet):
    authentication_classes = [
        SessionAuthentication, BasicAuthentication
    ]
    permission_classes = [AllowAny]
    View.http_method_names = ['get']

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