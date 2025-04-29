from django.urls import path
from django.views.generic import TemplateView
from main_app import views
from .views import ComingSoonView, UserProfileView, ProjectListCreateView, ProjectDetailView, ContactMessageCreateView, ContactView

urlpatterns = [
    path('', ComingSoonView.as_view(), name='coming-soon'),

    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/projects/', ProjectListCreateView.as_view(), name='projects'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('api/contact/', ContactMessageCreateView.as_view(), name='contact-message'),

    #form validation
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('success/', TemplateView.as_view(template_name='main_app/success.html'), name='success'),
]

