#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ComingSoonView(TemplateView):
    template_name = 'main_app/coming_soon.html'
