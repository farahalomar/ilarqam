# Generated by Django 3.1.5 on 2021-01-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='twitter_thread',
            field=models.URLField(),
        ),
    ]
