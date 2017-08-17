from time import time

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# CONSTANTES
CF_LOC_MAX      = 30
SEXE_MAX_L      = 5
TF_BIO_MAX_L    = 500.

SEXE_CHOICES    = (
    (1, 'Masc'),
    (2, 'Femm'),
            )

# Retourne le Nom De l'Image telechargee.
def get_upload_file_name(instance, filename):
    return "uploaded_files/profiles/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    photo       = models.FileField(upload_to=get_upload_file_name, blank=True)
    sexe        = models.IntegerField(choices=SEXE_CHOICES, default=1, help_text="Homme ou Femme?")
    bio         = models.TextField(max_length=TF_BIO_MAX_L, blank=True)
    location    = models.CharField(max_length=CF_LOC_MAX, blank=True)
    date_naiss  = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()