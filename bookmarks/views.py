from rest_framework import generics, permissions
from piehole_drf.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer, BookmarkDetailSerializer


class BookmarkList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkDetailSerializer
    queryset = Bookmark.objects.all()
