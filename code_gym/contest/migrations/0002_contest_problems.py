# Generated by Django 5.0.6 on 2024-06-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
        ('problems', '0005_submission_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='problems',
            field=models.ManyToManyField(to='problems.problem'),
        ),
    ]