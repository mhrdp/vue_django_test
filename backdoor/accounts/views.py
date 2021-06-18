from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import PremiumUser, Profile, RegisteredUser
from .serializers import (
    PremiumUserSerializer, ProfileSerializer,
    UserSerializer
    )
from ..decorators import superuser_only

# To get list of all users
class UserAPI(APIView):
    # admin only permission
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        username = RegisteredUser.objects.all()
        serializer = UserSerializer(username, many=True)
        return Response(serializer.data)


class UserRegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class PremiumUserAPI(APIView):
    permission_classes = [IsAdminUser]
    http_method_names = ['GET']

    def get(self, request, format=None):
        premium = PremiumUser.objects.filter(premium=True)
        serializer = PremiumUserSerializer(premium, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@superuser_only
def premium_user_api(request):
    premium = PremiumUser.objects.filter(premium=True)
    serializer = PremiumUserSerializer(premium, many=True)
    return Response(serializer.data)