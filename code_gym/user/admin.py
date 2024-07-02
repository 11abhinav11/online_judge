from django.contrib import admin
from .models import user


@admin.register(user)
class contestAdmin(admin.ModelAdmin):
    filter_horizontal = ("problems_solved", )
