from events import models
from rest_framework import generics, response

from . import serializers


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
