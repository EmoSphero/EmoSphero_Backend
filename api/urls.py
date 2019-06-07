from django.urls import path
from api import views

urlpatterns = [
    path('users/', views.list_users),
    path('user', views.find_or_create_user),
    path('scores/', views.get_scores),
    path('score', views.post_score)
]