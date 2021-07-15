from rest_framework import serializers

from .models import PostModel, ReferredPost
from ..accounts.serializers import PostUserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    # userdata is a pk because of ForeignKey relationship with RegisteredUser's model
    # I can't figure it out how to make it return the username without destroying the post's saving proccess
    class Meta:
        model = PostModel
        fields = [
            'id','userdata', 'post', 'slug', 'posted',
            'date_created', 'date_posted', 'get_absolute_url',
        ]
   
   # To show PostUserSerializer inside PostModelSerializer
   # If you not rewriting to_representation method, you'll get trouble when saving new data
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['userdata'] = PostUserSerializer(instance.userdata).data
        return rep

    def create(self, validated_data):
        return PostModel.objects.create(**validated_data)

class ReferredPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'userdata', 'referred_post', 'post', 'slug', 'posted',
            'date_created', 'date_posted'
        ]

    def to_representation(self, instance):
        rep = super().to_representaion(instance)
        rep['userdata'] = PostUserSerializer(instance.userdata).data
        return rep

    def create(self, validate_data):
        return ReferredPost.objects.create(**validated_data)
