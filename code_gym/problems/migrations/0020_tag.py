# Generated by Django 5.0.6 on 2024-07-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0019_remove_problem_tags_problem_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
    ]