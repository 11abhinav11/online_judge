# Generated by Django 5.0.6 on 2024-06-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_problem_difficulty_problem_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
