from django.contrib import admin

from .models import PostModel, CommunityOnlyPost, ReferredPost

# Register your models here.
admin.site.register(PostModel)
admin.site.register(CommunityOnlyPost)
admin.site.register(ReferredPost)
