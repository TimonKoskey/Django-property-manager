from django.urls import path
from .views import (
    MessageCreateAPIView,
    GetAllMessagesListAPIView,
    GetInboxMessagesListAPIView,
    GetOutboxMessagesListAPIView,
    GetNewMessagesListAPIView,
    MessageDetailsAPIView
)

urlpatterns = [
    path(r'create/', MessageCreateAPIView.as_view()),
    path(r'inbox/new/<int:user_id>/', GetNewMessagesListAPIView.as_view()),
    path(r'details/<int:pk>/', MessageDetailsAPIView.as_view()),
]
