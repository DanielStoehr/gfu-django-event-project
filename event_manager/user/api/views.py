from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer


class ListUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
