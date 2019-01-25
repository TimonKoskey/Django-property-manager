from django.urls import path
from .views import (
    PropertyListAPIView,
    PropertyCreateAPIView,
    UnitCreateAPIView,
    PropertyDetailsAPIView,
    UnitsListAPIView,
    UnitDetailsAPIView,
    AllPropertiesListAPIView,
    CreateUnitTenantAPIView,
    CreateUnitTenantRecords,
    CreateUnitTenantPaymentRecords
)

urlpatterns = [
    path(r'create/', PropertyCreateAPIView.as_view()),
    path(r'list/all', AllPropertiesListAPIView.as_view()),
    path(r'list/', PropertyListAPIView.as_view()),
    path(r'details/<int:pk>/',PropertyDetailsAPIView.as_view()),
    path(r'details/edit/<int:pk>/',PropertyDetailsAPIView.as_view()),
    path(r'details/delete/<int:pk>/',PropertyDetailsAPIView.as_view()),
    path(r'unit/create/', UnitCreateAPIView.as_view()),
    path(r'units/list/<int:prop_id>/', UnitsListAPIView.as_view()),
    path(r'unit/details/edit/<int:pk>/',UnitDetailsAPIView.as_view()),
    path(r'unit/tenant/register/<int:unit_id>/',CreateUnitTenantAPIView.as_view()),
    path(r'unit/tenant/records/create/<int:unit_id>/',CreateUnitTenantRecords.as_view()),
    path(r'unit/tenant/payment_records/create/<int:unit_id>/',CreateUnitTenantPaymentRecords.as_view()),
]
