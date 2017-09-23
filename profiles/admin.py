from django.contrib import admin
from profiles.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'cover', 'mobile', 'sexe', 'location','bio', 'date_naiss',]

admin.site.register(UserProfileModel, ProfileAdmin)
#
# user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
# mobile = models.IntegerField(unique=True, blank=True, null=True, help_text="Telephone Mobile.")
# photo = models.FileField(upload_to=get_upload_profile_photo_file_name, blank=True)
# cover = models.FileField(upload_to=get_upload_profile_cover_file_name, blank=True)
# sexe = models.IntegerField(choices=SEXE_CHOICES, default=2, help_text="Male or Female?")
# bio = models.TextField(max_length=TF_BIO_MAX_L, blank=True)
# location = models.CharField(max_length=CF_LOC_MAX, blank=True)
# date_naiss = models.DateField(null=True, blank=True)
# updated_on = models.DateTimeField('Joined On', auto_now_add=True, editable=False)
# slug = models.SlugField(blank=True, max_length=MAX_L_SLUG)