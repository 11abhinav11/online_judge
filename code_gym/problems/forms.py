from django import forms
from django.forms import ModelForm
from .models import problem, test_cases


class add_problem(ModelForm):
    # title = forms.CharField(max_length=150)
    # difficulty = forms.IntegerField()
    # tags = forms.CharField(max_length=50)
    # question = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = problem
        fields = ["title", "difficulty", "tags", "question"]


class add_test(ModelForm):
    # Input = forms.CharField(widget=forms.Textarea)
    # output = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = test_cases
        fields = ["Input", "output"]
