# Generated by Django 5.0.6 on 2024-06-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[('c++', 'c++'), ('python', 'python'), ('java', 'java'), ('c', 'c')], default='c++', max_length=20),
        ),
    ]
