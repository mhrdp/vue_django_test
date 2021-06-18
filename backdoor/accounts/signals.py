from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, PremiumUser

user_model = settings.AUTH_USER_MODEL
@receiver(post_save, sender=user_model)
def initialize_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)
        PremiumUser.objects.create(username=instance)

@receiver(post_save, sender=user_model)
def save_default_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.premiumuser.save()