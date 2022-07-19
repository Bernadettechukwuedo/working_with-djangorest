from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['title', 'body']

    def create(self, validated_data, **kwargs):
        user = kwargs['user']
        text = super().create(dict(user=user, **validated_data))
        return text
