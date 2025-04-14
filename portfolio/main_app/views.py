#from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from .models import UserProfile, Project, ContactMessage
from .serializers import UserProfileSerializer, ProjectSerializer, ContactMessageSerializer

# Create your views here.
class ComingSoonView(TemplateView):
    template_name = 'main_app/coming_soon.html'


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

