from django.urls import path
from .views import EmployeeAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Employee APIs
    path('employees/', EmployeeAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeAPIView.as_view(), name='employee-detail'),
]
