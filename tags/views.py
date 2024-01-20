from rest_framework import generics, permissions
from .models import Tag
from .serializers import TagSerializer

class TagList(generics.ListAPIView):
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