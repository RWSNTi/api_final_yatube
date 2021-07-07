from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title',)
        # согласно заданию нам нужно сделать проект на основе
        # проекта документации. В примерах запросов GET и CREATE в словаре
        # передаётся только значение по ключу "title",
        # другие ключи не используются.


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate_following(self, value):
        user = self.context['request'].user
        following = get_object_or_404(User, username=value)
        if user == following:
            raise serializers.ValidationError(
                "Запрещено подписываться на самого себя")
        return super().validate(value)

    class Meta:
        fields = ('following', 'user')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'user'],
            )
        ]
