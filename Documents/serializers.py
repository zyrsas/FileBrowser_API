from rest_framework import serializers
from Documents.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'latitude', 'longitude', 'date')