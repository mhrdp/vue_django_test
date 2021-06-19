from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    RegisteredUser, PremiumUser, Profile,
    MembersRoom, MembersRoomResident
    )

# Register your models here.
admin.site.register(PremiumUser)
admin.site.register(RegisteredUser, UserAdmin)
admin.site.register(Profile)
admin.site.register(MembersRoom)
admin.site.register(MembersRoomResident)