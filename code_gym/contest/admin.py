from django.contrib import admin
from .models import contest


@admin.register(contest)
class contestAdmin(admin.ModelAdmin):
    filter_horizontal = ("problems", )
