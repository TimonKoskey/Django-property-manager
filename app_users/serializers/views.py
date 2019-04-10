from django.contrib.auth import get_user_model
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from rest_framework_jwt.settings import api_settings

from app_users.models import (
    role_class,
    user_detail_class,
    location_class,
    company_management_class,
    tenant_details_class
)

from .serializers import (
    UserRoleSerializer,
    ExtendedUserDetailsSerailizer,
    ManagementCompanyDetailSerailizer,
    ManagementCompanyCreateSerailizer,
    CreateUserSerializer,
    CreateExtendedUserDetailsSerailizer,
    TenantSerializer
)

from rest_framework.generics import (
	CreateAPIView,
	RetrieveAPIView,
	ListAPIView,
	RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
	)

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
User = get_user_model()

class ManagementUsersLogin(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        mymeta = request.META.get('USER')
        serializer = ObtainJSONWebToken.get_serializer(self,data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            ext_user_obj = None
            if user_detail_class.objects.get(user=user):
                ext_user_obj = user_detail_class.objects.get(user=user)
            user_details = ExtendedUserDetailsSerailizer(ext_user_obj).data
            company_obj = company_management_class.objects.all()
            company_details = None
            if company_obj:
                company_details = ManagementCompanyDetailSerailizer(company_obj[0]).data
            response_data = [
                jwt_response_payload_handler(token, user, request),
                user_details,
                company_details
                ]
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True,
                                    )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TenantsLogin(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        mymeta = request.META.get('USER')
        serializer = ObtainJSONWebToken.get_serializer(self,data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            tenant_user_obj = None
            if tenant_details_class.objects.get(user=user):
                tenant_user_obj = tenant_details_class.objects.get(user=user)
            user_details = TenantSerializer(tenant_user_obj).data
            company_obj = company_management_class.objects.all()
            company_details = None
            if company_obj:
                company_details = ManagementCompanyDetailSerailizer(company_obj[0]).data
            response_data = [
                jwt_response_payload_handler(token, user, request),
                user_details,
                company_details
                ]
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True,
                                    )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateManagementCompanyAPIView (CreateAPIView):
    serializer_class = ManagementCompanyCreateSerailizer
    queryset = company_management_class.objects.all()

class ManagementCompanyDetailAPIView (RetrieveUpdateDestroyAPIView):
    serializer_class = ManagementCompanyDetailSerailizer
    queryset = company_management_class.objects.all()

class CreateUserAPIView (APIView):

    def post(self, request, *args, **kwargs):
        requestData= request.data
        role=requestData['role_id']
        if role == 'administrator':
            user_details=requestData['user_details']
            username = user_details['first_name']+user_details['last_name']
            user_details['username']= username.lower()
            user_serializer=CreateUserSerializer(data=user_details)
            if user_serializer.is_valid():
                user_obj = user_serializer.save()
                user_data = user_serializer
                extended_user_params={
                    'role_name': role
                }

                extended_user_serializer=CreateExtendedUserDetailsSerailizer(data=extended_user_params)
                if extended_user_serializer.is_valid():
                    extended_user_obj = extended_user_serializer.save()
                    extended_user_obj.user = user_obj
                    extended_user_obj.save()
                    extended_user_serializer = CreateExtendedUserDetailsSerailizer(extended_user_obj)
                    return Response(extended_user_serializer.data, status=status.HTTP_201_CREATED)
                return Response(extended_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('invalid role name', status=status.HTTP_400_BAD_REQUEST)



class AppUsersList(ListAPIView):
	serializer_class = ExtendedUserDetailsSerailizer

	def get_queryset(self, *args, **kwargs):
		role = self.request.GET.get('role_name')
		queryset = user_detail_class.objects.filter(role_name = role)
		return queryset



class AppUserDetails (RetrieveUpdateDestroyAPIView):
    serializer_class = user_detail_class
    queryset = user_detail_class.objects.all()

# class TenantCurrentUnitDetails ( APIView ):
