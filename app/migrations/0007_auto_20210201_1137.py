# Generated by Django 3.1.5 on 2021-02-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210201_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='lates_projects',
        ),
        migrations.AddField(
            model_name='person',
            name='lates_projects',
            field=models.ManyToManyField(to='app.Project'),
        ),
    ]
