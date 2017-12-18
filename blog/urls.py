from django.conf.urls import url

from .views import PostListView

urlpatterns = [
    url(r'^posts/$', PostListView.as_view(), name='posts'),
]
