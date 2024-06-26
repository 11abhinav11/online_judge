from django.db import models


class contest(models.Model):
    contest_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField(auto_created=True)
    number_of_problems = models.IntegerField()
