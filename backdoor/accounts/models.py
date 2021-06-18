from django.db import models
from django.utils import timezone

from PIL import Image
from io import BytesIO

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.
class RegisteredUser(AbstractUser):
    email = models.EmailField(_('Email Address'), blank=False, null=False)

    def get_absolute_url(self):
        return f'/{self.username}/{self.id}/'
    

class PremiumUser(models.Model):
    userdata = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    premium = models.BooleanField(default=False)
    date_become = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = f'{self.userdata}: {self.premium}'
        return format(template)

    def save(self, *args, **kwargs):
        if self.premium == True:
            self.date_become = timezone.now()
        else:
            self.date_become = None
        super(PremiumUser, self).save(*args, **kwargs)

class Profile(models.Model):
    userdata = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='img/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        profile = f'{self.userdata}\'s Profile'
        return format(profile)
    
    def get_image(self):
        if self.profile_pics:
            return f'/{self.profile_pics.url}/'

    def get_absolute_url(self):
        return f'/{self.userdata}/{self.id}/profile/'

    def resize_image(self, profile_pics, size=(150, 150)):
        img = Image.open(profile_pics)
        img.convert('RGB')
        img.thumbnail(size)

        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=85)
        profile_pics = InMemoryUploadedFile(
            img_io, 
            '$s.jpg' % profile_pics.name.split('.'),
            'image/jpeg'
        )

        return profile_pics
    
    
    