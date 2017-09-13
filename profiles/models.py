from time import time

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.urlresolvers import reverse
# CONSTANTES
from django.template.defaultfilters import slugify

CF_LOC_MAX      = 30
SEXE_MAX_L      = 5
TF_BIO_MAX_L    = 500.
MAX_L_SLUG      = 128

SEXE_CHOICES    = (
    (1, 'Female'),
    (2, 'Male'),
            )

# Retourne le Nom De l'Image telechargee.
def get_upload_photo_file_name(instance, filename):
    return "uploaded_files/profiles/members/%s_%s" % (str(time()).replace('.', '_'), filename)

def get_upload_cover_file_name(instance, filename):
    return "uploaded_files/profiles/covers/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile      = models.IntegerField(unique=True, blank=True, null=True, help_text="Telephone Mobile.")
    photo       = models.FileField(upload_to=get_upload_photo_file_name, blank=True)
    cover       = models.FileField(upload_to=get_upload_cover_file_name, blank=True)
    sexe        = models.IntegerField(choices=SEXE_CHOICES, default=2, help_text="Male or Female?")
    bio         = models.TextField(max_length=TF_BIO_MAX_L, blank=True)
    location    = models.CharField(max_length=CF_LOC_MAX, blank=True)
    date_naiss  = models.DateField(null=True, blank=True)
    joined_on   = models.DateTimeField('Joined On', auto_now_add=True, editable=False)
    slug        = models.SlugField(blank=True, max_length=MAX_L_SLUG)

    def __unicode__(self):
        return "%s" % self.user

    def get_absolute_url(self):
        return ('viewuserprofile',(), {'slug':self.slug})
        # return ('viewuserprofile',(), {'pk':self.pk})
        # return reverse('viewuserprofile', kwargs={'pk': self.pk})
        # return "/profile/view/%s" % self.pk
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.user.username)

    #
    # def natural_key(self):
    #     return (self.pk, self.user.username, self.slug, self.joined_on)

    class Meta:
        ordering = ('-joined_on',)
        unique_together = (('user', 'date_naiss', 'sexe', 'joined_on', 'slug'))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.create(user=instance)
        # Added for slug field.
        # prof.slug = slugify(prof.user.user)
        prof.slug = slugify(prof.user.username)
        prof.save()
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
