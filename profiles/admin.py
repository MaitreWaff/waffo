from django.contrib import admin
from profiles.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)