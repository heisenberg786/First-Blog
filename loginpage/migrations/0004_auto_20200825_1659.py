# Generated by Django 3.0.8 on 2020-08-25 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0003_login_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_page',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='login_page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]