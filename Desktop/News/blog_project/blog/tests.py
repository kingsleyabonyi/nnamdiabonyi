from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().object.create_user(
            username = 'testuser',
            email = 'kinabonyi@gmail.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user
        )

        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user
        )

        