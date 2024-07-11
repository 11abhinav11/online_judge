from django import forms
from django.forms import ModelForm
from .models import problem, test_cases, submission


class add_problem(ModelForm):
    class Meta:
        model = problem
        fields = ["title", "difficulty", "problem_tags", "question"]


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
                'id': 'code_editor',
                'name': 'code_editor',
                'style': 'max-width: 100%; display:none;  background-color: #222; max-height:350px; height: 200px; resize: none;',

            }),
            "test": forms.Textarea(attrs={
                'id': 'gg',
                'class': 'form-control border border-0 text-white example',
                'style': 'margin-left: 15px; max-width: 60%; background-color: #333; max-height:100px; height:100px; resize: none;',
            }),
            "language": forms.Select(attrs={
                'class': 'form-control border border-0 text-white form-select',
                'style': 'max-width: 100px; background-color: #222;',
                'id': 'lang'
            })
        }
