from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from v1.views import Health

urlpatterns = [
    path(
        "health/",
        Health.as_view(),
    ),
    path(
        "token/",
        TokenObtainPairView.as_view(),
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
    ),
]
