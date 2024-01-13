# Import necessary modules
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer
from pp5_api.permissions import IsOwnerOrReadOnly  # Assuming you have a similar permission class for comments

# Create CommentList APIView
class CommentList(APIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create CommentDetail APIView
class CommentDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]  # Use appropriate permission class for comments
    serializer_class = CommentSerializer

    def get_object(self, post_pk, comment_pk):
        try:
            comment = Comment.objects.get(post__pk=post_pk, pk=comment_pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, post_pk, comment_pk):
        # Retrieve a specific comment for a specific post
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def put(self, request, post_pk, comment_pk):
        # Update a specific comment for a specific post
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, comment_pk):
        # Delete a specific comment for a specific post
        comment = self.get_object(post_pk, comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
