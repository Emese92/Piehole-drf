from rest_framework import serializers
from .models import Recipe
from likes.models import Like
from bookmarks.models import Bookmark

# This Serializer was created based on the example project of Code Institute


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger then 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger then 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger then 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, recipe=obj
            ).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, recipe=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'title', 'prep_time', 'image', 'is_owner', 'number_of_portions',
            'ingredients', 'steps', 'profile_id',
            'profile_image', 'like_id', 'bookmark_id',
            ]
