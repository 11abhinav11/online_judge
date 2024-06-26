from django.contrib import admin
from .models import problem, test_cases, submission

admin.site.register(problem)
admin.site.register(test_cases)
admin.site.register(submission)
