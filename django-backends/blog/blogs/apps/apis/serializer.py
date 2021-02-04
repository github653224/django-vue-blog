from abc import ABC
import datetime

from rest_framework import serializers
from .models import Blog, BlogCatgory, BlogComment, Messages, FriendsLink, Music
import markdown2


class IndexBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'summary', 'publish_time', 'category_name', 'clicks']


class CommentsRelatedFileds(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return '{"email":"%s**@%s", "content":"%s", "create_time":"%s"}' % (
            value.emails[0:2], value.emails.split('@')[-1], value.content,
            datetime.datetime.strftime(value.create_time, '%Y-%m-%d'))


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'summary', 'publish_time', 'category_name', 'contents', 'clicks', 'comments']

    def get_comments(self, obj):
        return BlogCommentsSerializer(BlogComment.objects.filter(blog_id=obj.id), many=True).data


class BlogCommentsSerializer(serializers.ModelSerializer):
    emails = serializers.CharField(max_length=50, write_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogComment
        exclude = []

    def create(self, validated_data):
        new_comment = BlogComment.objects.create(**validated_data)
        new_comment.content = markdown2.markdown(new_comment.content, extras=['fenced-code-blocks'])
        new_comment.save()
        return new_comment

    def get_email(self, obj):
        return obj.emails[0:3] + "***" + obj.emails.split("@")[-1]


class CategoryDetailSerializer(serializers.ModelSerializer):
    blogs = serializers.SerializerMethodField()

    class Meta:
        model = BlogCatgory
        fields = ['id', 'name', 'blogs']

    def get_blogs(self, obj):
        return IndexBlogSerializer(Blog.objects.filter(category=obj.id), many=True).data


class MessageSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(read_only=True)
    emails = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = Messages
        exclude = []

    def get_email(self, obj):
        return obj.emails[0:3] + "***" + obj.emails.split("@")[-1]


class FriendsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsLink
        exclude = []


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = []
