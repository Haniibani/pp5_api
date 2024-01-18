from django import forms
from rest_framework import generics, permissions
from .models import Tag
from .serializers import TagSerializer

class TagListForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer(self, *args, **kwargs):
        """
        Override the default get_serializer method to use TagListForm
        for creating a new tag.
        """
        if self.request.method == 'POST':
            return TagListForm(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        """
        Override perform_create to handle the creation of a new tag.
        """
        if self.request.method == 'POST':
            tags_data = self.request.data.getlist('name', [])
            for tag_name in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                serializer.instance.tags.add(tag)
        else:
            serializer.save()

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]