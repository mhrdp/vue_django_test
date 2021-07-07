from rest_framework import serializers

from .models import PostModel
from ..accounts.serializers import UserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    # userdata is a pk because of ForeignKey relationship with RegisteredUser's model
    # I can't figure it out how to make it return the username without destroying the post's saving proccess
    class Meta:
        model = PostModel
        fields = [
            'id','userdata', 'post', 'referred', 'slug', 'posted',
            'date_created', 'date_posted', 'get_absolute_url',
        ]

    def create(self, validated_data):
        return PostModel.objects.create(**validated_data)
