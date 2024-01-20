from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post
from tags.models import Tag
import json


class PostTests(TestCase):
    def setUp(self):
        # Set up a test user and log in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        # Manually create a post and associate predefined tags with it
        self.post = Post.objects.create(owner=self.user, title='Test Post', content='Test Content')
        self.tag1 = Tag.objects.get(name='Technology')
        self.tag2 = Tag.objects.get(name='Travel')
        self.post.tags.add(self.tag1, self.tag2)

    def test_create_post(self):
        # Test retrieving a specific post and verify it has the correct number of tags
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        post_response_data = json.loads(response.content)
        self.assertEqual(len(post_response_data.get('tags', [])), 2)

    def test_get_post_list(self):
        # Test retrieving the list of posts
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_detail(self):
        # Test retrieving the details of a specific post
        post = Post.objects.create(owner=self.user, title='Test Post')
        response = self.client.get(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        # Test updating a post's title
        post = Post.objects.create(owner=self.user, title='Test Post')
        updated_data = {'title': 'Updated Test Post'}
        response = self.client.patch(f'/posts/{post.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        # Test deleting a post
        post = Post.objects.create(owner=self.user, title='Test Post')
        response = self.client.delete(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
