from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from rest_framework import generics
from .models import UserProfile, Project, ContactMessage
from .serializers import UserProfileSerializer, ProjectSerializer, ContactMessageSerializer

# Create your views here.
class ComingSoonView(TemplateView):
    template_name = 'main_app/base.html'


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


#Form validation view
class ContactView(FormView):
    template_name = 'base.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
