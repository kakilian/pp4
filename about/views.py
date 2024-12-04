from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.obejects.all()
    template_name = "about/post_list.html"
