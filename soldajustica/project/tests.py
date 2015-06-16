from django.test import TestCase
from django.contrib.auth.models import User
from .models import (
    Project
)

class PostTestCase(TestCase):

    def test_create(self):
        project = Project()
        project.name = 'My first post'
        project.description = 'This is my first post'
        project.save()