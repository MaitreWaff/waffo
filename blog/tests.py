from django.contrib.auth.models import User
from django.test import TestCase

from blog.views import home
from .models import Blog
#from django.utils import timezone
from django.core.urlresolvers import reverse, resolve


#from profiles.tests import ProfileTest
# Create your tests here.

# models test
class BlogTest(TestCase):

    def create_blog(self, profile, theme='Premier Theme du Blog.'):
        blg = Blog.objects.create(auteur=profile, theme=theme)
        return blg

    def test_blog_creation(self, ):
        # prof = ProfileTest.create_profile()
        # blg = self.create_blog(prof)
        # self.assertEqual(blg.theme, 'Premier Theme du Blog.')
        pass


# View test

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)















