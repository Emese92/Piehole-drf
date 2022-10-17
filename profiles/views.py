from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from piehole_drf.permissions import IsOwnerOrReadOnly

# This model view was created based on the example project of Code Institute


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
        bookmarks_count=Count('owner__bookmark', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'recipes_count',
        'bookmarks_count'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
        bookmarks_count=Count('owner__bookmark', distinct=True)
    ).order_by('-created_at')
