from django.db import models
from problems.models import problem


class contest(models.Model):
    contest_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField(auto_now_add=True)
    number_of_problems = models.IntegerField()
    problems = models.ManyToManyField(problem, blank=True)
