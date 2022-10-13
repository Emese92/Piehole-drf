from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from piehole_drf.permissions import IsOwnerOrReadOnly

# This model view was created based on the example project of Code Institute


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
