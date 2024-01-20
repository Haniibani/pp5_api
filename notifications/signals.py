from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Notification
from posts.models import Post
from comments.models import Comment 
from likes.models import Like
from followers.models import Follower 

# For creating comment notifications
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,  # Use 'owner' instead of 'author'
            message=f"New comment on your post by {instance.owner.username}",
            notification_type='comment',
            related_object_id=instance.post.id
        )

# For creating like notifications
@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,  # Use 'owner' instead of 'author'
            message=f"Your post was liked by {instance.owner.username}",
            notification_type='like',
            related_object_id=instance.post.id
        )

# For creating follower notifications
@receiver(post_save, sender=Follower)
def create_follower_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.followed,
            message=f"You have a new follower: {instance.owner.username}",  # Use 'owner' instead of 'follower'
            notification_type='follower',
            related_object_id=instance.owner.id
        )

