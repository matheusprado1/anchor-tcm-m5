from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status
from .mixins import SerializerByMethodMixin
from .models import User
from .serializers import LoginSerializer, UserSerializer, ListUserSerializer


class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = User.objects.all().order_by("username")
    serializer_map = {
        "GET": ListUserSerializer,
        "POST": UserSerializer
    }


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    lookup_url_kwarg = "user_id"

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(
            {"detail": "Invalid email or password"},
            status.HTTP_400_BAD_REQUEST,
        )
