from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import MySpecialJWT,LoginDetails

urlpatterns = [
    path(r'api-token-auth/', MySpecialJWT.as_view()),
    path(r'login-details/<int:pk>/',LoginDetails.as_view())
]
