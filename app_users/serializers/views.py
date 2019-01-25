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
)

from .serializers import (
    UserRoleSerializer,
    ExtendedUserDetailsSerailizer,
    ManagementCompanyDetailSerailizer,
    ManagementCompanyCreateSerailizer,
    CreateUserSerializer,
    CreateExtendedUserDetailsSerailizer
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

class MySpecialJWT(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        mymeta = request.META.get('USER')
        serializer = ObtainJSONWebToken.get_serializer(self,data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            ext_user_obj = user_detail_class.objects.get(user=user)
            user_details = ExtendedUserDetailsSerailizer(ext_user_obj).data
            company_obj = company_management_class.objects.all()
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
        user_details=requestData['user_details']
        user_details['username']=user_details['first_name']+user_details['last_name']
        user_serializer=CreateUserSerializer(data=user_details)
        if user_serializer.is_valid():
            user_serializer.save()
            user_data=user_serializer.data
            extended_user_params={
                'user': user_data['id'],
                'role': role,
            }
            print(extended_user_params)

            extended_user_serializer=CreateExtendedUserDetailsSerailizer(data=extended_user_params)
            if extended_user_serializer.is_valid():
                user_obj=User.objects.get(id= user_data['id'])
                role_obj=role_class.objects.get(id=role)
                extended_user_obj = user_detail_class(user=user_obj,role=role_obj)
                extended_user_obj.save()
                extended_user_serializer = CreateExtendedUserDetailsSerailizer(extended_user_obj).data
                print(extended_user_serializer)
                return Response(extended_user_serializer, status=status.HTTP_201_CREATED)
            return Response(extended_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AppUsersList(ListAPIView):
	serializer_class = ExtendedUserDetailsSerailizer

	def get_queryset(self, *args, **kwargs):
		role = self.request.GET.get('role_name')
		role_obj=role_class.objects.get(role_name = role)
		queryset = user_detail_class.objects.filter(role = role_obj)
		return queryset



class AppUserDetails (RetrieveUpdateDestroyAPIView):
    serializer_class = user_detail_class
    queryset = user_detail_class.objects.all()
