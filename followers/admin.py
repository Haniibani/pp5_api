from django.contrib import admin
from .models import Follower  # Adjust the import according to your app structure

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed', 'created_at')  # Customize as needed
    search_fields = ('owner__username', 'followed__username')