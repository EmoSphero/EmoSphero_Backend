from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
from api.models import Score, ApiUser as User


@api_view(["GET"])
def list_users(request):
    users = User.objects.all()
    user_list = [{"username": u.username, "id": u.id} for u in users]
    return Response(status=status.HTTP_200_OK, data=user_list)


@api_view(["POST"])
def find_or_create_user(request):
    print(f"Got data {request.data}")
    # request_user = json.loads(request.data['user'])
    request_username = request.data["user"]
    db_user = User.objects.filter(username=request_username)
    if len(db_user):
        return Response(data={"id": db_user[0].id})
    else:
        new_user = User.objects.create_user(request_username)
        new_user.save()
        return Response(status=status.HTTP_200_OK,
                        data={"username": new_user.username})


@api_view(["GET"])
def get_scores(request):
    scores = Score.objects.all()
    score_list = [{"score": s.score, "id": s.user_id} for s in scores]
    return Response(status=status.HTTP_200_OK, data=score_list)


@api_view(["POST"])
def post_score(request):
    print(request.data)
    # request_score_data = json.loads(request.data)
    user = User.objects.get(id=int(request.data['user_id']))
    score = int(request.data['score'])
    new_score = Score.objects.create(user=user, score=score)
    new_score.save()
    return Response(status=status.HTTP_200_OK, data={new_score.to_json()})
