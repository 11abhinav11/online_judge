from django.contrib import admin
from .models import problem, test_cases, submission, save_code

admin.site.register(test_cases)
admin.site.register(submission)
admin.site.register(save_code)
admin.site.register(problem)
