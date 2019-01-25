from django.urls import path
from .views import (
    MySpecialJWT,
    CreateManagementCompanyAPIView,
    ManagementCompanyDetailAPIView,
    CreateUserAPIView,
    AppUsersList,
    # AppUserDetails
)

urlpatterns = [
    path(r'api-token-auth/', MySpecialJWT.as_view()),
    path(r'company/create/', CreateManagementCompanyAPIView.as_view()),
    path(r'company/details/<int:pk>/', ManagementCompanyDetailAPIView.as_view()),
    path(r'user/create/', CreateUserAPIView.as_view()),
    path(r'users/list/', AppUsersList.as_view()),
    # path(r'user/details/<int:pk>/', AppUserDetails.as_view()),
]
