from rest_framework import serializers, validators
from .models import Conference, Role, ConfUser
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['id', 'name']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class ConfUserSerializer(serializers.ModelSerializer):
    conferences = serializers.PrimaryKeyRelatedField(many=True, queryset=Conference.objects.all())
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = ConfUser
        fields = ['id', 'name', 'email', 'conferences', 'role']
        depth = 1
