from django.db import models
from django.contrib.auth.models import User
from problems.models import problem


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    problems_solved = models.ManyToManyField(problem, blank=True)
