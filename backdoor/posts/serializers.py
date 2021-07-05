from rest_framework import serializers

from .models import PostModel
from ..accounts.serializers import UserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    # userdata = UserSerializer()
    
    # This is to limit what to be show from external model
    # userdata is the name of the field that hold User model
    # that has 1-to-1 relationship with Profile model
    username = serializers.CharField(source='userdata.username')
    
    class Meta:
        model = PostModel
        fields = [
            'id','username','post', 'referred', 'slug', 'posted',
            'date_created', 'date_posted', 'get_absolute_url',
        ]

    def create(self, validated_data):
        return PostModel.objects.create(**validated_data)
        