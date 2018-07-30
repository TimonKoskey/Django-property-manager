from django.urls import path
from .views import (
    PropertyListAPIView,
    PropertyDetailsAPIView
    )

urlpatterns = [
    path(r'list/',PropertyListAPIView.as_view()),
    path(r'details/<int:pk>/',PropertyDetailsAPIView.as_view()),
]
