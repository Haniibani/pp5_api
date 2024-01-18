from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    predefined_tags = [
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Fashion', 'Fashion'),
        ('Art', 'Art'),
        ('Science', 'Science'),
        ('Health', 'Health'),
        ('Music', 'Music'),
        ('Sports', 'Sports'),
        ('Nature', 'Nature'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Photography', 'Photography'),
        ('History', 'History'),
        ('Literature', 'Literature'),
        ('Movies', 'Movies'),
        ('Gaming', 'Gaming'),
        ('Cooking', 'Cooking'),
        ('Fitness', 'Fitness'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_11111', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'