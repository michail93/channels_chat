from django.conf.urls import url
from django.urls import path
from .consumers import AsyncChatConsumer

websocket_urlpatterns = [
    path("ws/blog/", AsyncChatConsumer)
]

