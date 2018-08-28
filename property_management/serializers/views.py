from property_management.models import (
    property_class,
    unitdetail_class,
    )

from userAuthentication.models import (
    agency_class,
    superadmin_class,
    admin_class,
    tenant_class,
    location_class,
    avatar_class
)

from .serializers import (
    PropertiesListSerializer,
    PropertyDetailsSerializer
)

from rest_framework.generics import (
	CreateAPIView,
	RetrieveUpdateAPIView,
	ListAPIView,
	RetrieveAPIView,
	)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	IsAdminUser,
	)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User=get_user_model()

class PropertyListAPIView( ListAPIView ):

	serializer_class = PropertiesListSerializer

	def get_queryset(self,*args,**kwargs):
		queryset = []
		auth = self.request.META
		# print(auth)
		user_ID = int(self.request.GET.get('user'))
		permission = self.request.GET.get('permission')
		user_obj = User.objects.get(id = user_ID)

		if permission == '3':
			super_admin = superadmin_class.objects.get(User_details = user_obj)
			queryset = property_class.objects.filter(Agency= super_admin.Agency_details)

		if permission == '2':
			admin = admin_class.objects.filter(User_details = user_obj)
			queryset = property_class.objects.filter(Administrator=admin)

		return queryset

class PropertyDetailsAPIView ( RetrieveAPIView ):
	queryset = property_class
	serializer_class = PropertyDetailsSerializer

	# def perfom_retrieve(self,serializer):
	# 	print (self.request.user)
