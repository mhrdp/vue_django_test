from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

from ..accounts.models import RegisteredUser, MembersRoom
from ..functions import get_random_slug

min_length_validation_msg = 'You probably need more characters'
class PostModel(models.Model):
    # Public's posts Model
    userdata = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    post = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=300, 
                message=min_length_validation_msg
                )
            ]
        )
    slug = models.SlugField(max_length=16, null=True, blank=True, unique=True)
    posted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now())
    date_posted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.userdata}\'s Post #{self.slug}'

    def save(self, *args, **kwargs):
        # Generate random slug / identifier
        get_random_slug(self)

        if self.posted == True:
            self.date_posted = timezone.now()
        else:
            self.date_posted = None
        
        super(PostModel, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/post/{self.userdata.username}/{self.slug}/'

class ReferredPost(models.Model):
    userdata = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    referred_post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    post = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=300,
                message=min_length_validation_msg
            )
        ]
    )
    slug = models.SlugField(max_length=16, null=True, blank=True, unique=True)
    posted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now())
    date_posted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.userdata}\'s referal #{self.slug}'

    def save(self, *args, **kwargs):
        get_random_slug(self)
        if self.posted == True:
            self.date_posted = timezone.now()
        else:
            self.date_posted = None
        super(ReferredPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/post/{self.userdata.username}/{self.slug}/referto/{self.referred_post.slug}/'

class CommunityOnlyPost(models.Model):
    # Member only post model
    userdata = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, null=True)
    post = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=300,
                message='You probably need more characters!'
            )
        ]
    )

    member_tier = models.ForeignKey(
        MembersRoom, on_delete=models.CASCADE,
        null=False, blank=False
    )

    slug = models.SlugField(max_length=16, null=True, blank=True, unique=True)
    posted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now())
    date_posted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.userdata}\'s Post #{self.slug}'

    def save(self, *args, **kwargs):
        # Generate random slug / identifier
        get_random_slug(self)

        if self.posted == True:
            self.date_posted = timezone.now()
        else:
            self.date_posted = None
        
        super(PostModel, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/post/member/{self.slug}/'
