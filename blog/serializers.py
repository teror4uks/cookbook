from rest_framework import serializers
from .models import Post

'''
'user',
'title',
'slug',
'image',      
'height_field',
'width_field', 
'content',
'draft',
'publish',
'read_time', 
'updated',
'timestamp',
'''

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'user',
            'title',
            'slug',
            'image',      
            'height_field',
            'width_field', 
            'publish',
            'read_time', 
            'updated',
        )

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'user',
            'title',
            'slug',
            'image',      
            'height_field',
            'width_field', 
            'content',
            'draft',
            'publish',
            'read_time', 
            'updated',
            'timestamp',
        )
