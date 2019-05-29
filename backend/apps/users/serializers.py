from rest_framework import serializers

from django.conf import settings

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(
        format='%H:%M %d.%m.%Y', read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)

    def get_full_name(self, obj):
        return obj.full_name

    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'registered_at']


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']


class UserApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
