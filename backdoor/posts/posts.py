from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import View

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView
)

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import PostModel
from .serializers import PostModelSerializer

# Create your views here.
class CreatePostView(CreateAPIView):
    # Default behaviour
    def post(self, request):
        serializer = PostModelSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response('Success')
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)


# Get specific user's post
class GetUserPostView(APIView):
    serializer_class = PostModelSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return PostModel.objects.filter(
            userdata__username=username
        )