from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    job = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'