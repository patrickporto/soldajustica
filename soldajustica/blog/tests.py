from django.test import TestCase
from django.contrib.auth.models import User
from .models import (
    Post
)

class PostTestCase(TestCase):

    def test_create(self):
        user = User.objects.create_user(
            username="test",
            password="test",
            email="test@test.com",
        )

        post = Post()
        post.author = user
        post.title = 'My first post'
        post.content = 'This is my first post'
        post.published = True
        post.save()