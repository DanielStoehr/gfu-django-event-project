from events import models
from rest_framework import authentication, exceptions, generics, response

from . import serializers
from .permissions import IsPublicOrAdmin


class ServiceUnavailible(exceptions.APIException):
    status_code = 503
    default_detail = "Something went wrong"


def save_category(request_serializer):
    request_serializer.is_valid(raise_exception=True)
    request_serializer.save()
    response_serializer = serializers.CategoryResponseSerializer(
        request_serializer.data
    )
    return response.Response(response_serializer.data)


class CategoryListAPIView(generics.ListCreateAPIView):
    """
    list: public
    create: Adminuser (Token, Session)

    response soll CategoryResponseSerializer sein
    """

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [IsPublicOrAdmin]
    authentication_classes = [authentication.SessionAuthentication]

    def create(self, request, *args, **kwargs):
        request_serializer = self.serializer_class(data=request.data)
        return save_category(request_serializer=request_serializer)


class CategoryUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    list: public
    create: Adminuser (Token, Session)

    response soll CategoryResponseSerializer sein
    """

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [IsPublicOrAdmin]
    authentication_classes = [authentication.SessionAuthentication]

    def update(self, request, *args, **kwargs):
        category = self.get_object()
        request_serializer = self.serializer_class(category, data=request.data)
        return save_category(request_serializer=request_serializer)

    def partial_update(self, request, *args, **kwargs):
        category = self.get_object()
        request_serializer = self.serializer_class(
            category, data=request.data, partial=True
        )
        return save_category(request_serializer=request_serializer)


class EventListAPIView(generics.ListCreateAPIView):
    # serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.prefetch_related("reviews__author")
    authentication_classes = [authentication.SessionAuthentication]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.EventInputSerializer
        return serializers.EventOutputSerializer

    def perform_create(self, serializer):
        # raise ServiceUnavailible() #  eigene Exception
        author = self.request.user
        print(author)
        serializer.save(author=author)
