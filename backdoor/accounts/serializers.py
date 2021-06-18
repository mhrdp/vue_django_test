from rest_framework import serializers

from .models import RegisteredUser, PremiumUser, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'user_permissions', 'is_staff', 'is_active', 'is_superuser',
            'last_login', 'date_joined',
        ]

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    userdata = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            'url', 'id', 'userdata', 'get_image', 'get_absolute_url',
            'bio',
        ]

class PremiumUserSerializer(serializers.HyperlinkedModelSerializer):
    userdata = UserSerializer()

    class Meta:
        model = PremiumUser
        fields = [
            'url', 'id', 'userdata', 'premium', 'date_become', 
        ]