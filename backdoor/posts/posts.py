from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import View

from rest_framework import serializers

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveAPIView
)

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import PostModel
from .serializers import PostModelSerializer

# Create your views here.
class CreatePostView(ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

# Get specific user's post
class GetUserPostView(ListAPIView):
    serializer_class = PostModelSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return PostModel.objects.filter(
            userdata__username=username
        )

class GetDetailPostView(RetrieveAPIView):
    serializer_class = PostModelSerializer
    
    # Return an object instance for detailed view
    # detail here: https://bit.ly/3h5wPKV
    def get_object(self, post_username, post_slug):
        try:
            return PostModel.objects.filter(
                userdata__username=post_username
            ).get(
                slug=post_slug
            )
        except PostModel.DoesNotExist:
            raise Http404
    
    # Get the object, pay attention to the url router
    def get(self, request, post_username, post_slug, format=None):
        queryset = self.get_object(post_username, post_slug)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)