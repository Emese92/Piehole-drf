from rest_framework import generics, permissions
from .models import Recipe
from .serializers import RecipeSerializer
from piehole_drf.permissions import IsOwnerOrReadOnly

# This view was created based on the example project of Code Institute


class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recipe.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
