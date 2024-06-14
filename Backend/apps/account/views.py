from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import LoginSerializer
from .utils import get_tokens_for_user

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        data = request.data
        serializer = LoginSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = get_tokens_for_user(user)

        return Response(
            {
                'status' : 200,
                'msg' : 'login successful',
                'token' : token
            }
        )

