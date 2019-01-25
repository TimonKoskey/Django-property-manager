from django.contrib import admin
from .models import (
    role_class,
    user_detail_class,
    location_class,
    company_management_class,
    tenant_details_class,
    tenants_record_class,
    tenant_payment_record
)

admin.site.register(location_class)
admin.site.register(company_management_class)
admin.site.register(role_class)
admin.site.register(user_detail_class)
admin.site.register(tenant_details_class)
admin.site.register(tenants_record_class)
admin.site.register(tenant_payment_record)
