from rest_framework import serializers
from .models import UserProfile, Project, ContactMessage

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = ContactMessage
        fields = '__all__'

