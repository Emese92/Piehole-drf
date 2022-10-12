from rest_framework import generics, permissions
from piehole_drf.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# This view was created based on the example project of Code Institute


class LikeList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
