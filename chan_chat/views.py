from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Post

# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "chan_chat/blog.html", {"posts": posts})
