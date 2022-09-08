from django.contrib.auth import authenticate
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status

from .mixins import SerializerByMethodMixin
from .models import User
from .serializers import ListUserSerializer, LoginSerializer, UserSerializer


class UserFilter(filters.FilterSet):
    name = filters.CharFilter("first_name", "icontains")

    class Meta:
        model = User
        fields = []


class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_map = {"GET": ListUserSerializer, "POST": UserSerializer}

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter


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
