from django.contrib.auth.models import User
from django.test import TestCase
from .models import Blog
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.

# models test
class BlogTest(TestCase):

    def create_blog(self, profile, theme='Premier Theme du Blog.'):
        blg = Blog.objects.create(auteur=profile, theme=theme)
        return blg

    def test_blog_creation(self, ):