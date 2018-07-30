from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from userAuthentication.models import classNames
from rest_framework_jwt.settings import api_settings

from userAuthentication.models import (
    agency_class,
    superadmin_class,
    admin_class,
    tenant_class,
    location_class,
    avatar_class
)

from .serializers import (
    AgencySuperAdminDetailsSerializer,
    AgencyAdminDetailsSerializer
)

from django.contrib.auth import get_user_model

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
user=get_user_model()

class MySpecialJWT(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        mymeta = request.META.get('USER')
        print (mymeta)
        serializer = ObtainJSONWebToken.get_serializer(self,data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            permission_status = 1
            if classNames['AdministratorClass'].objects.filter(User_details = user.id):
                permission_status = 2
            if classNames['SuperAdministratorClass'].objects.filter(User_details = user.id):
                permission_status = 3
            response_data = [
                jwt_response_payload_handler(token, user, request),
                {'status':permission_status,'id':user.id}
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

class LoginDetails ( APIView ):

    def get (self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user_obj = user.objects.get(id = user_id)
        print (dir(user_obj))
        serializer = []

        serializer_obj = superadmin_class.objects.filter(User_details = user_obj)
        if serializer_obj:
            serializer = AgencySuperAdminDetailsSerializer(serializer_obj,many=True).data

        serializer_obj = admin_class.objects.filter(User_details = user_obj)
        if serializer_obj:
            serializer = AgencyAdminDetailsSerializer(serializer_obj,many=True).data

        return Response(serializer)
