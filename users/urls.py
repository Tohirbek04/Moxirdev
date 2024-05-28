from django.urls import path

from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserListCreateAPIView.as_view()),
    path('user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view())
]