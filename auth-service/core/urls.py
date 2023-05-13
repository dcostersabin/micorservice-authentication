from django.urls import re_path, include

urlpatterns = [
    re_path(r"^v1/", include(("v1.urls", "v1"), namespace="v1")),
]
