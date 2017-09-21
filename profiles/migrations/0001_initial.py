# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(blank=True, help_text=b'Telephone Mobile.', null=True, unique=True)),
                ('photo', models.FileField(blank=True, upload_to=profiles.models.get_upload_profile_photo_file_name)),
                ('cover', models.FileField(blank=True, upload_to=profiles.models.get_upload_profile_cover_file_name)),
                ('sexe', models.IntegerField(choices=[(1, b'Female'), (2, b'Male')], default=2, help_text=b'Male or Female?')),
                ('bio', models.TextField(blank=True, max_length=500.0)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('date_naiss', models.DateField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Joined On')),
                ('slug', models.SlugField(blank=True, max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userprofilemodel',
            unique_together=set([('user', 'date_naiss', 'sexe', 'slug')]),
        ),
    ]
