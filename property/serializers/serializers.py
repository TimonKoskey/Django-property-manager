from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from property.models import (
    property_class,
    unitdetail_class,
    UnitPictures_class,
)

from app_users.serializers.serializers import(
	ExtendedUserDetailsSerailizer,
	LocationSerializer,
	TenantSerializer,
	# CreateUserSerializer,
	TenantRecordSerializer,
	PaymentRecordSerializer
	)

class PropertyCreateSerializer (ModelSerializer):

	class Meta:
		model = property_class
		fields = [
            'property_name',
            # 'location',
            'property_type',
			# 'property_overview_photo',
			'occupied_units',
			'number_of_units',
			'availlable_units'
		]

class PropertyListSerializer (ModelSerializer):
	location=SerializerMethodField()
	administrator = SerializerMethodField()

	class Meta:
		model=property_class
		fields=[
			'id',
            'property_name',
            'location',
            'property_type',
			'property_overview_photo',
			'administrator'
        ]
	def get_administrator (self,obj):
		administrator=ExtendedUserDetailsSerailizer(obj.administrator).data
		return administrator

	def get_location (self,obj):
		location=LocationSerializer(obj.location).data
		return location

class PropertyDetailSerializer (ModelSerializer):
	administrator = SerializerMethodField()
	class Meta:
		model=property_class
		fields=[
			'id',
            'property_name',
            'location',
            'property_type',
			'property_overview_photo',
			'administrator',
			'occupied_units',
			'number_of_units',
			'availlable_units'
        ]
	def get_administrator (self,obj):
		administrator=ExtendedUserDetailsSerailizer(obj.administrator).data
		return administrator

class UnitCreateSerializer (ModelSerializer):

	class Meta:
		model = unitdetail_class
		fields = [
			'propertyDetail',
		    'unit_ID',
		    'unit_size',
		    'number_of_rooms',
		    'unit_value',
		]

class UnitsListSerializer (ModelSerializer):
	tenant_details=SerializerMethodField()
	tenant_records=SerializerMethodField()
	tenant_current_month_payment_status=SerializerMethodField()
	pictures=SerializerMethodField()
	class Meta:
		model = unitdetail_class
		fields = [
			'id',
		    'unit_ID',
		    'unit_size',
		    'number_of_rooms',
		    'unit_value',
		    'unit_purpose',
		    'tenant_details',
		    'tenant_records',
		    'tenant_current_month_payment_status',
			'pictures'
		]

	def get_tenant_details(self, obj):
		tenant_details=TenantSerializer(obj.tenant_details).data
		return tenant_details

	def get_tenant_records(self, obj):
		tenant_records=TenantRecordSerializer(obj.tenant_records).data
		return tenant_records

	def get_tenant_current_month_payment_status(self, obj):
		tenant_current_month_payment_status=PaymentRecordSerializer(obj.tenant_current_month_payment_status).data
		return tenant_current_month_payment_status

	def get_pictures(self, obj):
		pictures_queryset=UnitPictures_class.objects.filter(unit_ID=obj)
		pictures=UnitsPicturesListSerializer(pictures_queryset, many=True).data
		return pictures

class UnitsPicturesListSerializer(ModelSerializer):

	class Meta:
		model=UnitPictures_class
		fields=[
			'pictures'
		]

# class UnitDetailsSerializer (ModelSerializer):
#
# 	class Meta:
# 		model = unitdetail_class
# 		fields = [
# 			'id',
# 		    'unit_ID',
# 		    'unit_size',
# 		    'number_of_rooms',
# 		    'unit_value',
# 		]

class TenantDetailsSerializer (ModelSerializer):
	tenant_records=SerializerMethodField()
	tenant_current_month_payment_status=SerializerMethodField()
	class Meta:
		model = unitdetail_class
		fields = [
			# 'id',
		    'unit_ID',
		    'unit_size',
		    'number_of_rooms',
		    'unit_value',
		    'unit_purpose',
		    'tenant_records',
		    'tenant_current_month_payment_status',
		]

	def get_tenant_records(self, obj):
		tenant_records=TenantRecordSerializer(obj.tenant_records).data
		return tenant_records

	def get_tenant_current_month_payment_status(self, obj):
		tenant_current_month_payment_status=PaymentRecordSerializer(obj.tenant_current_month_payment_status).data
		return tenant_current_month_payment_status
