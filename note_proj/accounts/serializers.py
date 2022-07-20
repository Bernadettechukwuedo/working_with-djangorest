from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def validate(self, data):
        user = authenticate(**data)

        if user:
            data['user'] = user

        else:
            data['user'] = AnonymousUser

        return data
