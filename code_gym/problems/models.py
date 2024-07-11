from django.db import models
from django.contrib.auth.models import User


class problem(models.Model):
    diff = (('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'))

    Problem_ID = models.AutoField(primary_key=True)
    problem_tags = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=150)
    question = models.TextField()
    date = models.DateField(auto_now_add=True)
    difficulty = models.CharField(max_length=20, choices=diff, default='easy')
    solved = models.IntegerField(default=0)


class test_cases(models.Model):
    Test_ID = models.AutoField(primary_key=True)
    Problem_ID = models.ForeignKey("problem", on_delete=models.CASCADE)
    Input = models.TextField()
    output = models.TextField()


class submission(models.Model):
    lang = (('cpp', 'C++'), ('py', 'Python'), ('js', 'JavaScript'), ('c', 'C'))

    Sub_ID = models.AutoField(primary_key=True)
    code = models.TextField(default="")
    test = models.TextField(default="", blank=True, null=True)
    language = models.CharField(max_length=20, choices=lang, default='c++')
    verdict = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now_add=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Problem_Id = models.ForeignKey("problem", on_delete=models.CASCADE)


class save_code(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Problem_Id = models.ForeignKey("problem", on_delete=models.CASCADE)
    code = models.TextField(default="")
