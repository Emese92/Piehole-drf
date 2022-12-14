from rest_framework import serializers
from .models import Profile

# This serializer was created based on the example project of Code Institute


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    recipes_count = serializers.ReadOnlyField()
    bookmarks_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner',
            'recipes_count', 'bookmarks_count',
            ]
