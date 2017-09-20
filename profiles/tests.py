from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserProfileModel
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your tests here.

# models test
class ProfileTest(TestCase):

    def create_profile(self, username="waluc", email="waffoluc@yahoo.com"):
        user = User.objects.create(username=username, email=email)
        pf = UserProfileModel.objects.get(user=user)
        pf.location = 'Bertoua'
        pf.save()
        return pf

    def test_profile_creation(self):
        pf = self.create_profile()
        self.assertTrue(isinstance(pf, UserProfileModel))
        self.assertEqual(pf.__unicode__(), pf.user.username)
        self.assertEqual(pf.location, 'Bertoua')


