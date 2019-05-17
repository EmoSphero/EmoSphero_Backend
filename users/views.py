from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from . import models
from . import serializers
# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


@api_view(["GET"])
def book(request):
    books = [
        "Pro Python", "Fluent Python", "Speaking javascript",
        "The Go programming language"
    ]
    return Response(status=status.HTTP_200_OK, data={"data": books})
