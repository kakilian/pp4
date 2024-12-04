from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(author=1)
    template_name = "about/templates/about/post_list.html"
