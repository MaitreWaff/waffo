from django.db import models

# CONSTANTES
MAX_L_TITRE = 150

# Create your models here.


class BlogPost(models.Model):
    title       = models.CharField(max_length=MAX_L_TITRE)
    body        = models.TextField()
    timestamp   = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

