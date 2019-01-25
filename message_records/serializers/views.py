from django.contrib.auth import get_user_model
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from rest_framework.generics import (
	CreateAPIView,
	RetrieveAPIView,
	ListAPIView,
	RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
	)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	IsAdminUser,
	)

from .serializers import (
    MessageCreateSerializer,
    MessagesListSerializer,
    MessageDetailsSerializer
)

from message_records.models import message_class

class MessageCreateAPIView (CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = message_class.objects.all()

class MessagesListAPIView (ListAPIView):
    serializer_class = MessagesListSerializer

    def get_queryset(self,*args,**kwargs):
        user_id = self.request.GET
        print (user_id)
        queryset=message_class.objects.all()
		# property_class.objects.get(id=user_id)
        return queryset

class MessageDetailsAPIView (RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailsSerializer
    queryset = message_class
