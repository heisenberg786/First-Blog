# Generated by Django 3.0.8 on 2020-08-25 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0005_remove_login_page_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_page',
            name='bio',
        ),
    ]