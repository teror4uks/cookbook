from rest_framework import viewsets, mixins
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, 
                  viewsets.GenericViewSet):

    queryset = Post.objects.active()
    serializer_class = PostListSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return super().get_serializer_class()

