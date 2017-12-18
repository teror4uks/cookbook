from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from .models import Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

