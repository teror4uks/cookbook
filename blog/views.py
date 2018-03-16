from rest_framework import viewsets, mixins
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.active()
    serializer_class = PostListSerializer


