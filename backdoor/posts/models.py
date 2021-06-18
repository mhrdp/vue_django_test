from django.db import models
from django.core.validators import MinLengthValidator

from ..accounts.models import RegisteredUser
from ..functions import get_random_slug

import datetime
# Create your models here.
class PostModel(models.Model):
    min_length_validation_msg = 'You probably need more than that to elaborate yout thought!'

    userdata = models.ForeignKey(RegisteredUser, on_delete=models.PROTECT)
    post = models.TextField(
        validators=[
            MinLengthValidator(
                limit_value=150, 
                message=min_length_validation_msg
                )
            ]
        )
    slug = models.SlugField(max_length=16, null=True, blank=True)
    posted = models.BooleanField(default=False)
    date_created = models.DateField(default=datetime.date.today())
    date_posted = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.userdata}\'s Post'

    def save(self, *args, **kwargs):
        get_random_slug(self)

        if self.posted == True:
            self.date_posted = datetime.date.today()
        else:
            self.date_posted = None
        
        super(PostModel, self).save(*args, **kwargs)