from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# CONSTANTES
CF_LOC_MAX      = 30
TF_BIO_MAX_L    = 500.

# Create your models here.

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
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