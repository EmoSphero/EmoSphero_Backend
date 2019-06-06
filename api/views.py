import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# This will return a list of books
@api_view(["GET"])
def book(request):
    books = [
        "Pro Python", "Fluent Python", "Speaking javascript",
        "The Go programming language"
    ]
    return Response(status=status.HTTP_200_OK, data={"data": books})


@api_view(["GET"])
def list_users(request):
    return Response(status=status.HTTP_200_OK,
                    data={"username": "test username"})


@api_view(["POST"])
def find_or_create_user(request):
    print(f"Got data {request.data}")
    user = json.loads(request.data['user'])
    username = user['username']
    return Response(status=status.HTTP_200_OK,
                    data={"user_id": "1", "username": username})
