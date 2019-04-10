from django.contrib.auth import get_user_model
from app_users.models import (
    role_class,
    user_detail_class,
    location_class,
    company_management_class,
    tenant_details_class,
    tenants_record_class,
    tenant_payment_record,
)

from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

User = get_user_model()
from django.core.mail import send_mail

class UserSerializer (ModelSerializer):
    class Meta:
        model=User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]

class CreateUserSerializer (ModelSerializer):
    class Meta:
        model=User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def create (self, validated_data):
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        username=validated_data['username']
        email=validated_data['email']

        user_obj=User(first_name=first_name, last_name=last_name,username=username, email=email)
        user_passwd=User.objects.make_random_password()
        user_obj.set_password(user_passwd)
        user_obj.save()
        # send_mail(
        #         'SakaAdmin login credentials',
        #         'username: %s  password: %s' %(user_obj.username,user_passwd),
        #         'timonkoskey@gmail.com',
        #         ['%s' %(user_obj.email)]
        #     )
        return user_obj

    def update (self, instance, validated_data):
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name', instance.last_name)
        instance.username=validated_data.get('username', instance.username)
        instance.email=validated_data.get('email',instance.email)

        instance.save(update_fields=['first_name', 'last_name',
            'username', 'email'])

        return instance

class UserRoleSerializer (ModelSerializer):

    class Meta:
        model=role_class
        fields=[
            'id',
            'role_name',
            'date_created'
        ]

class ExtendedUserDetailsSerailizer (ModelSerializer):
    user = SerializerMethodField()
    # role = SerializerMethodField()

    class Meta:
        model=user_detail_class
        fields=[
            'id',
            'user',
            'role_name',
            'date_created',
            'mobile_number'
            ]
    def get_user(self,obj):
        user = UserSerializer(obj.user).data
        return user

class CreateExtendedUserDetailsSerailizer (ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model=user_detail_class
        fields=[
            'user',
            'role_name',
            'mobile_number'
            ]
    def get_user(self,obj):
        user = UserSerializer(obj.user).data
        return user

class ManagementCompanyCreateSerailizer (ModelSerializer):

    class Meta:
        model = company_management_class
        fields = [
            'company_name',
            'location',
            'email',
            'phone_number',
            'physical_address',
        ]

class ManagementCompanyDetailSerailizer (ModelSerializer):

    class Meta:
        model=company_management_class
        fields=[
            'id',
            'company_name',
            'location',
            'email',
            'phone_number',
            'physical_address',
        ]

class LocationSerializer (ModelSerializer):

    class Meta:
        model=location_class
        fields=[
            'county',
            'city_or_town',
            'area_or_estate_name',
            'street_name',
            'buiding_nam',
        ]

class TenantSerializer(ModelSerializer):
    user=SerializerMethodField()
    class Meta:
        model=tenant_details_class
        fields=[
            'id',
            'user',
            'phone_number',
            'occupation',
            'relationship_status',
            'emergency_contact_name',
            'emergency_contact_relationship',
            'emergency_contact_phone_number'
        ]

    def get_user(self,obj):
        user=UserSerializer(obj.user).data
        return user

    def create (self, validated_data):
        phone_number=validated_data['phone_number']
        occupation=validated_data['occupation']
        relationship_status=validated_data['relationship_status']
        emergency_contact_name=validated_data['emergency_contact_name']
        emergency_contact_relationship=validated_data['emergency_contact_relationship']
        emergency_contact_phone_number=validated_data['emergency_contact_phone_number']

        tenant_obj=tenant_details_class(phone_number=phone_number, occupation=occupation, relationship_status=relationship_status,
        emergency_contact_name=emergency_contact_name, emergency_contact_relationship=emergency_contact_relationship,
        emergency_contact_phone_number=emergency_contact_phone_number)

        tenant_obj.save()
        return tenant_obj

    def update (self, instance, validated_data):
        instance.phone_number=validated_data['phone_number']
        instance.occupation=validated_data['occupation']
        instance.relationship_status=validated_data['relationship_status']
        instance.emergency_contact_name=validated_data['emergency_contact_name']
        instance.emergency_contact_relationship=validated_data['emergency_contact_relationship']
        instance.emergency_contact_phone_number=validated_data['emergency_contact_phone_number']

        instance.save()

        return instance

class TenantRecordSerializer (ModelSerializer):

    class Meta:
        model=tenants_record_class
        fields=[
            'date_of_entry',
            'date_of_exit'
        ]

class PaymentRecordSerializer( ModelSerializer ):

    class Meta:
        model=tenant_payment_record
        fields=[
            'expected_amount',
            'amount_paid',
            'balance',
            'mode_of_payment',
            'date_of_payment',
            'payment_status'
        ]

    def create(self,validated_data):
        expected_amount=validated_data['expected_amount']
        amount_paid=validated_data['amount_paid']
        balance=validated_data['balance']
        mode_of_payment=validated_data['mode_of_payment']
        payment_status=validated_data['payment_status']

        tenant_payment_record_obj=tenant_payment_record(expected_amount=expected_amount,amount_paid=amount_paid,
        balance=balance,mode_of_payment=mode_of_payment,payment_status=payment_status)
        tenant_payment_record_obj.save()
        return tenant_payment_record_obj

    def update (self, instance, validated_data):
        instance.expected_amount=validated_data.get('expected_amount',instance.expected_amount)
        instance.amount_paid=validated_data.get('amount_paid', instance.amount_paid)
        instance.balance=validated_data.get('balance', instance.balance)
        instance.mode_of_payment=validated_data.get('mode_of_payment',instance.mode_of_payment)
        # instance.date_of_payment=validated_data.get('date_of_payment',
        # instance.payment_status=validated_data.get('payment_status',instance.payment_status)

        instance.save()

        return instance

# class TenantDetailsSerializer (ModelSerializer):
#
#     class META:
#         model =
