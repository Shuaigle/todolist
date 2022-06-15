from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):

    # we don't send password back to frontend -> write only
    # add limitations of password creation
    password = serializers.CharField(
        max_length=255, min_length=4, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    # 'password' was set to write only, and will not return
    # some may send extra info -> **validated_data
    # serializer.save() 
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=255, min_length=4, write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')
        read_only_fields = ['token']
    