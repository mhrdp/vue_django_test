from rest_framework import serializers

from .models import RegisteredUser, PremiumUser, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = [
            'id', 'username', 'password', 'email', 'first_name', 'last_name',
            'user_permissions', 'is_staff', 'is_active', 'is_superuser',
            'last_login', 'date_joined',
        ]
    
    # hash the password on create so Django could read it
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_active = validated_data.pop('is_active', True)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    # hash the password on update
    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            if attr == 'password':
                instance.set_password(val)
            else:
                setattr(instance, attr, val)
        instance.save()
        return instance

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