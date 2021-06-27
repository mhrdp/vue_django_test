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
        
        read_only_fields = (
            'is_active', 'is_staff', 'is_superuser',
            'last_login', 'date_joined'
        )
        
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    
    # hash the password on create so Django could read it
    # validated_data is a built-in authentication of DRF, it return querysets similar to Django
    # the format is {ModelName: {Key: {Value}}, ...}
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

class ProfileSerializer(serializers.ModelSerializer):
    # userdata = UserSerializer()
    
    # This is to limit what to be show from external model
    # userdata is the name of the field that hold User model
    # that has 1-to-1 relationship with Profile model
    username = serializers.CharField(source='userdata.username')
    

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'get_image', 'get_absolute_url',
            'bio',
        ]

class PremiumUserSerializer(serializers.ModelSerializer):
    # userdata = UserSerializer()
    
    # This is to limit what to be show from external model
    # userdata is the name of the field that hold User model
    # that has 1-to-1 relationship with Profile model
    username = serializers.CharField(source='userdata.username')

    class Meta:
        model = PremiumUser
        fields = [
            'id', 'username', 'premium', 'date_become', 
        ]