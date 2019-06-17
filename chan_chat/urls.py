from django.urls import path, re_path
from .views import blog_index

urlpatterns = [
    path("blog/", blog_index, name="room"),
]