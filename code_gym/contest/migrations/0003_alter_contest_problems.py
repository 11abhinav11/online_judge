# Generated by Django 5.0.6 on 2024-06-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_contest_problems'),
        ('problems', '0005_submission_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='problems',
            field=models.ManyToManyField(blank=True, to='problems.problem'),
        ),
    ]
