from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.active()

