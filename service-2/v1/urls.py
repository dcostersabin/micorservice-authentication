from django.urls import path
from v1.views import Health
from v1.views import ProtectedView


urlpatterns = [
    path(
        "health/",
        Health.as_view(),
    ),
    path(
        "protected/",
        ProtectedView.as_view(),
    ),
]
