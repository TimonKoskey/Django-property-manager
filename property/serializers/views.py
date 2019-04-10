from django.contrib.auth import get_user_model
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from django.contrib.contenttypes.models import ContentType
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
    PropertyListSerializer,
    PropertyDetailSerializer,
	PropertyCreateSerializer,
	UnitCreateSerializer,
	UnitsListSerializer,
	TenantDetailsSerializer
)

from property.models import (
    property_class,
    unitdetail_class,
    UnitPictures_class,
)

from app_users.serializers.serializers import (
	TenantSerializer,
	CreateUserSerializer,
	TenantRecordSerializer,
	PaymentRecordSerializer
)

from app_users.models import (
    role_class,
    user_detail_class,
    location_class,
    company_management_class,
    tenant_details_class,
    tenants_record_class,
    tenant_payment_record,
)

# print (role_id)


# property_class.objects.get(id=user_id)

class PropertyCreateAPIView (CreateAPIView):
	serializer_class = PropertyCreateSerializer
	queryset = property_class.objects.all()

class AllPropertiesListAPIView (ListAPIView):
	queryset=property_class.objects.all()
	serializer_class = PropertyListSerializer

class PropertyListAPIView (ListAPIView):
    serializer_class = PropertyListSerializer

    def get_queryset(self,*args,**kwargs):
    	admin_id = self.kwargs['admin_id']
    	admin_obj = user_detail_class.objects.get(id=admin_id)
    	queryset=property_class.objects.filter(administrator = admin_obj)
    	return queryset

class PropertyDetailsAPIView (RetrieveUpdateDestroyAPIView):
	serializer_class = PropertyDetailSerializer
	queryset = property_class.objects.all()

class UnitCreateAPIView (CreateAPIView):
	serializer_class = UnitCreateSerializer
	queryset = unitdetail_class.objects.all()

class UnitsListAPIView (ListAPIView):
	serializer_class = UnitsListSerializer

	def get_queryset(self, *args, **kwargs):
		prop_id = self.kwargs['prop_id']
		property_obj=property_class.objects.get(id=prop_id)
		queryset = unitdetail_class.objects.filter(propertyDetail=property_obj)
		return queryset

class UnitDetailsAPIView (RetrieveUpdateDestroyAPIView):
	serializer_class = UnitsListSerializer
	queryset = unitdetail_class.objects.all()

# class EditUnitTenantDetails (APIView):
#
# 	def post (self, request, *args, **kwargs):
# 		unit_id = kwargs['unit_id']
# 		tenant_data = request.data
# 		unit_obj=unitdetail_class.objects.get(id=unit_id)
# 		unit_tenant_obj = unit_obj.tenant_details
#
		# user_data_serializer = User

class CreateUnitTenantAPIView(APIView):

	def post (self, request, *args, **kwargs):
		unit_id=kwargs['unit_id']
		tenant_data = request.data
		user_class_data = tenant_data['user_info']
		tenant_class_details=tenant_data['tenant_class_details']

		tenant_class_details_serializer=TenantSerializer(data=tenant_class_details)
		if tenant_class_details_serializer.is_valid():
			saved_tenant_class_obj=tenant_class_details_serializer.create(tenant_class_details_serializer.validated_data)

			user_clas_data_serializer=CreateUserSerializer(data=user_class_data)
			if user_clas_data_serializer.is_valid():
				saved_user_class_obj=user_clas_data_serializer.create(user_clas_data_serializer.validated_data)
				saved_tenant_class_obj.user = saved_user_class_obj
				saved_tenant_class_obj.save()
				tenant_class_details_serializer=TenantSerializer(saved_tenant_class_obj)

				return Response(tenant_class_details_serializer.data, status=status.HTTP_201_CREATED)
		return Response(tenant_class_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateUnitTenantDetailsAPIView(APIView):

	def post (self, request, *args, **kwargs):
		unit_id=kwargs['unit_id']
		unit_obj=unitdetail_class.objects.get(id=unit_id)

		tenant_data = request.data
		unit_tenant_obj = unit_obj.tenant_details

		user_class_data = tenant_data['user_data']
		tenant_class_details=tenant_data['tenant_class_details']

		tenant_class_details_serializer=TenantSerializer(data=tenant_class_details)
		if tenant_class_details_serializer.is_valid():
			new_tenant_class_obj=tenant_class_details_serializer.update(unit_tenant_obj, tenant_class_details_serializer.validated_data)

			user_clas_data_serializer=CreateUserSerializer(data=user_class_data)
			old_user_data_obj=unit_tenant_obj.user
			new_user_obj=user_clas_data_serializer.update(old_user_data_obj, user_clas_data_serializer.initial_data)
			new_tenant_class_obj.user=new_user_obj
			new_tenant_class_obj.save()

			tenant_class_details_serializer=TenantSerializer(new_tenant_class_obj)

			return Response(tenant_class_details_serializer.data, status=status.HTTP_201_CREATED)
		return Response(tenant_class_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUnitTenantRecords(APIView):

	def post (self, request, *args, **kwargs):
		unit_id=kwargs['unit_id']
		# tenant_id=kwargs['tenant_id']
		unit_obj=unitdetail_class.objects.get(id=unit_id)
		unit_contenttype=ContentType.objects.get_for_model(unit_obj)
		tenant_details_obj=unit_obj.tenant_details

		tenant_records_obj=tenants_record_class(
		    tenant=tenant_details_obj,
		    unit_contenttype=unit_contenttype,
		    unit_object_id=unit_id
		)

		tenant_records_obj.save()
		unit_obj.tenant_records=tenant_records_obj
		unit_obj.save()

		serializer=TenantRecordSerializer(tenant_records_obj)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateUnitTenantPaymentRecords(APIView):

	def post (self, request, *args, **kwargs):
		unit_id=kwargs['unit_id']
		# tenant_record_id=kwargs['tenant_record_id']
		unit_obj=unitdetail_class.objects.get(id=unit_id)
		unit_contenttype=ContentType.objects.get_for_model(unit_obj)
		tenant_record_details_obj=unit_obj.tenant_records
		payment_records_data=request.data
		payment_records_serializer=PaymentRecordSerializer(data=payment_records_data)
		if payment_records_serializer.is_valid():
			saved_payment_records_obj=payment_records_serializer.create(payment_records_serializer.validated_data)
			saved_payment_records_obj.tenant_record_obj=tenant_record_details_obj
			saved_payment_records_obj.unit_object_id = unit_id
			unit_contenttype=ContentType.objects.get_for_model(unit_obj)
			saved_payment_records_obj.unit_contenttype=unit_contenttype
			saved_payment_records_obj.save()
			unit_obj.tenant_current_month_payment_status=saved_payment_records_obj
			unit_obj.save()
			saved_payment_records_serializer=PaymentRecordSerializer(saved_payment_records_obj)
			return Response(saved_payment_records_serializer.data, status=status.HTTP_201_CREATED)
		return Response(saved_payment_records_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUnitPaymentRecords (APIView):

	def post (self, request, *args, **kwargs):
		unit_id = kwargs['unit_id']
		unit_obj=unitdetail_class.objects.get(id=unit_id)
		payment_record_obj = unit_obj.tenant_current_month_payment_status

		payment_records_data = request.data

		payment_records_data_serializer = PaymentRecordSerializer(data=payment_records_data)
		print(payment_records_data)
		if payment_records_data_serializer.is_valid():
			payment_records_data_serializer.update(payment_record_obj, payment_records_data_serializer.validated_data)
			return Response(payment_records_data_serializer.data, status=status.HTTP_201_CREATED)
		return Response(payment_records_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTenant (APIView):

	def post (self, request, *args, **kwargs):
		unit_id = kwargs['unit_id']
		unit_obj=unitdetail_class.objects.get(id=unit_id)

		unit_obj.tenant_details = None
		unit_obj.tenant_records =None
		unit_obj.tenant_current_month_payment_status = None

		unit_obj.save()
		unit_obj_serializer = UnitsListSerializer(unit_obj)
		return Response(unit_obj_serializer.data, status=status.HTTP_201_CREATED)

class GetTenantDetails ( APIView ):

	def get (self, request, *args, **kwargs):
		tenant_id = kwargs['tenant_id']
		tenant_obj = tenant_details_class.objects.get(id=tenant_id)
		unit_obj = unitdetail_class.objects.filter(tenant_details = tenant_obj)[0]
		serializer = TenantDetailsSerializer(unit_obj)
		return Response (serializer.data, status=status.HTTP_200_OK)
