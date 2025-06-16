from rest_framework.views import APIView
from validate.serializers import PasswordValidationSerializer
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status



class PasswordValidationview(views.APIView):
    def post(self, request):
        serializer = PasswordValidationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"detail": "Password is valid."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

