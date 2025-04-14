from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/')
    tech_stack = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
