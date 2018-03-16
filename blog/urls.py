from django.conf.urls import url, include
from rest_framework import routers
from .views import PostViewSet

app_name = 'blog'

router = routers.DefaultRouter()

router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    url(r'^blog/', include(router.get_urls()))
]
