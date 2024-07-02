from django.db import models
from django.contrib.auth.models import User


class problem(models.Model):
    Problem_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    question = models.TextField()
    tags = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    difficulty = models.IntegerField(default=100)
    solved = models.IntegerField(default=0)


class test_cases(models.Model):
    Test_ID = models.AutoField(primary_key=True)
    Problem_ID = models.ForeignKey("problem", on_delete=models.CASCADE)
    Input = models.TextField()
    output = models.TextField()


class submission(models.Model):
    lang = (('cpp', 'c++'), ('py', 'python'), ('java', 'Java'), ('c', 'C'))
    Sub_ID = models.AutoField(primary_key=True)
    code = models.TextField()
    language = models.CharField(max_length=20, choices=lang, default='c++')
    verdict = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now_add=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Problem_Id = models.ForeignKey("problem", on_delete=models.CASCADE)
    test_case = models.TextField()
