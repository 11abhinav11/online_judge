from django import forms
from django.forms import ModelForm
from .models import problem, test_cases, submission


class add_problem(ModelForm):

    class Meta:
        model = problem
        fields = ["title", "difficulty", "tags", "question"]


class add_test(ModelForm):

    class Meta:
        model = test_cases
        fields = ["Input", "output"]


class question_form(ModelForm):

    class Meta:
        model = submission
        fields = ["language", "code", "test"]
        widgets = {
            "code": forms.Textarea(attrs={
                'class': 'form-control border border-0 text-white',
                'style': 'max-width: 100%; background-color: #222; max-height:350px; height: 400px; resize: none;',

            }),
            "test": forms.Textarea(attrs={
                'class': 'form-control border border-0 text-white',
                'style': 'max-width: 35%; background-color: #333; max-height:130px; resize: none;',
            }),
            "language": forms.Select(attrs={
                'class': 'form-control border border-0 text-white',
                'style': 'max-width: 100px; background-color: #333;'
            })
        }
