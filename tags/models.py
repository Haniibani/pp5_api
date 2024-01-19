# models.py
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_predefined_tags(cls):
        predefined_tags = [
            'Technology',
            'Travel',
            'Food',
            'Fashion',
            'Art',
        ]

        for tag_name in predefined_tags:
            cls.objects.get_or_create(name=tag_name)

# Run create_predefined_tags method to add predefined tags
Tag.create_predefined_tags()
