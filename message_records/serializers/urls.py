from django.urls import path
from .views import (
    MessageCreateAPIView,
    MessagesListAPIView,
    MessageDetailsAPIView
)

urlpatterns = [
    path(r'message/create/', MessageCreateAPIView.as_view()),
    path(r'messages/list/', MessagesListAPIView.as_view()),
    path(r'message/details/<int:pk>/', MessageDetailsAPIView.as_view()),
]
