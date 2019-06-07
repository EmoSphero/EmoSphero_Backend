from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
import json


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username):
        user = self.model(username=username)
        user.set_password("foo")
        user.save(using=self._db)
        return user


class ApiUser(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'

    email = models.CharField(max_length=200, unique=True)
    EMAIL_FIELD = 'email'
    objects = MyUserManager()


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def to_json(self):
        return json.dumps({
            "username": self.user.username,
            "user_id": self.user.id,
            "score": self.score,
            "date": self.date.isoformat()
        })
