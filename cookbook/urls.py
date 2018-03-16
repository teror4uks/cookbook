from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

main = [
    url(r'^v1/', include('blog.urls', namespace='blog_v1')),
]

urlpatterns = [
    url(r'api/', include(main)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(url(r'^api-map/$', get_swagger_view(title='Api map')))

try:
    urlpatterns.append(url(r'^', TemplateView.as_view(template_name='base.html'), name='index'))
except TemplateDoesNotExist:
    pass