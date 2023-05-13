from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class Health(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        return Response({"status": "If You See This Service 2 Is Running"})


class ProtectedView(APIView):
    def get(self, request):
        return Response({"Service 2 Received User ID": self.request.user.pk})
