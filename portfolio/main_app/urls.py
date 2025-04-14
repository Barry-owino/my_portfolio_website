from django.urls import path
from .views import ComingSoonView, UserProfileView, ProjectistCreateView, ProjectDetailView, ContactMessageCreateView

urlpatterns = [
    path('', ComingSoonView.as_view(), name='coming-soon'),

    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/projects/', ProjectListCreateView.as_view(), name='projects'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('api/contact/', ContactMessageCreateView.as_view(), name='contact-message'),
]

