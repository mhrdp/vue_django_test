from django.db import models
from django.core.validators import MinLengthValidator

from ..accounts.models import RegisteredUser, MembersRoom
from ..functions import get_random_slug

import datetime

class PostModel(models.Model):
    # Public's posts Model
    min_length_validation_msg = 'You probably need more than that to elaborate yout thought!'

    userdata = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    post = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=300, 
                message=min_length_validation_msg
                )
            ]
        )
    referred = models.IntegerField(default=0)
    slug = models.SlugField(max_length=16, null=True, blank=True)
    posted = models.BooleanField(default=False)
    date_created = models.DateField(default=datetime.date.today())
    date_posted = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.userdata}\'s Post #{self.slug}'

    def save(self, *args, **kwargs):
        # Generate random slug / identifier
        get_random_slug(self)

        if self.posted == True:
            self.date_posted = datetime.date.today()
        else:
            self.date_posted = None
        
        super(PostModel, self).save(*args, **kwargs)

class CommunityOnlyPost(models.Model):
    # Member only post model
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    member_tier = models.ForeignKey(
        MembersRoom, on_delete=models.CASCADE,
        null=False, blank=False
        )
    is_restricted = models.BooleanField(default=False)

    def __str__(self):
        return f'Post #{self.id} RESTRICT'
