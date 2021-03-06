from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

        def save(self):
            super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)