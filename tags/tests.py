from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Tag
from .serializers import TagSerializer

class TagSerializerTestCase(TestCase):
    def test_serializer_with_valid_data(self):
        """
        Test that the serializer can serialize Tag instances with valid data.
        """
        tag_data = {'name': 'Test Tag'}
        serializer = TagSerializer(data=tag_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test Tag')

    def test_serializer_with_empty_data(self):
        """
        Test that the serializer is not valid when 'name' is missing.
        """
        serializer = TagSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

class TagListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.predefined_tag_names = [
            'Technology', 'Travel', 'Food', 'Fashion', 'Art',
            'Science', 'Health', 'Music', 'Sports', 'Nature',
            'Business', 'Education', 'Photography', 'History',
            'Literature', 'Movies', 'Gaming', 'Cooking', 'Fitness'
        ]
        cls.predefined_tags = [
            Tag.objects.get(name=tag_name) for tag_name in cls.predefined_tag_names
        ]

    def setUp(self):
        self.client = APIClient()
        self.url = '/tags/'  # Replace 'tag-list' with the name of your URL pattern

    def test_list_tags(self):
        """
        Test that the API returns a list of predefined tags.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Since the response is paginated, we check the length of results on the first page
        returned_tags = response.data.get('results', [])
        self.assertEqual(len(returned_tags), 10)  # Expecting 10 tags on the first page

        # Optionally, you can also test if the total count of tags is as expected
        self.assertEqual(response.data.get('count'), len(self.predefined_tags))


    def test_create_tag(self):
        """
        Test creating a new tag using POST request (expecting 405 method not allowed).
        """
        data = {'name': 'New Tag'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

