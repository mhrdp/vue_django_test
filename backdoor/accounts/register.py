from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import RegisteredUser
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes(AllowAny)
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            RegisteredUser.objects.create(
                serializer.data['username'],
                serializer.data['email'],
                serializer.data['first_name']
            )

