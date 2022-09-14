from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import APIView, Response, status

from .mixins import SerializerByMethodMixin
from .models import Image, User
from .permissions import IsUserAdmin, IsUserOwner
from .serializers import (
    ImageSerializer,
    ListUserSerializer,
    LoginSerializer,
    UserSerializer,
)


class UserFilter(filters.FilterSet):
    is_staff = filters.BooleanFilter("is_staff")

    class Meta:
        model = User
        fields = []


class UserView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [IsUserAdmin]

    queryset = User.objects.all().order_by("created_at")
    serializer_map = {"GET": ListUserSerializer, "POST": UserSerializer}

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOwner]

    lookup_url_kwarg = "user_id"

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ImageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "user_id"

    def perform_create(self, serializer):

        user = get_object_or_404(User, id=self.kwargs["user_id"])
        serializer.save(user=user)


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
