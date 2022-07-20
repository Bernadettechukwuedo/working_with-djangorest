from lib2to3.pgen2 import token
from rest_framework.views import APIView
from .utils import get_user_token
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


# Create your views here.


class LoginView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        data = get_user_token(user)
        print(data)
        return Response(data, status=status.HTTP_200_OK)
