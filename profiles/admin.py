from django.contrib import admin
from profiles.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'cover', 'mobile', 'sexe', 'location','bio', 'date_naiss', 'updated_on']

admin.site.register(UserProfileModel, ProfileAdmin)


