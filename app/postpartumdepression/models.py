from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Question(models.Model):
    query = models.CharField(max_length=250)


    def __str__(self):
        return self.query


class Answer(models.Model):
    answer = models.CharField(max_length=250)
    points = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.answer

