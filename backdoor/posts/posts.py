from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import View

from rest_framework import serializers

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveAPIView
)

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import PostModel
from .serializers import PostModelSerializer

# Create your views here.
class CreatePostView(APIView):
    def post(self, request, format=None):
        data = request.data
        data['userdata'] = request.user.pk

        serializer = PostModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        queryset = PostModel.objects.all()
        serializer = PostModelSerializer(queryset, many=True)
        return Response(serializer.data)

# Get specific user's post
class GetUserPostView(ListAPIView):
    serializer_class = PostModelSerializer
    
    def get_queryset(self):
        # get username's value from URL, refer to urls.py
        username_pk = self.kwargs['pk']
        return PostModel.objects.filter(
            userdata=username_pk
        )

class GetDetailPostView(RetrieveAPIView):
    serializer_class = PostModelSerializer
    
    # Return an object instance for detailed view
    # detail here: https://bit.ly/3h5wPKV
    def get_object(self, post_username_pk, post_slug):
        try:
            return PostModel.objects.filter(
                userdata=post_username_pk
            ).get(
                slug=post_slug
            )
        except PostModel.DoesNotExist:
            raise Http404
    
    # Get the object, pay attention to the url router
    def get(self, request, post_username_pk, post_slug, format=None):
        queryset = self.get_object(post_username_pk, post_slug)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
