from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class Health(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        return Response({"status": "If You See This Service 1 Is Running"})


class ProtectedView(APIView):
    def get(self, request):
        return Response({"Service 1 Received User ID": self.request.user.pk})
