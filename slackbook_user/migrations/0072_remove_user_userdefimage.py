# Generated by Django 3.2.18 on 2023-04-29 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0071_alter_user_userdefimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userDefImage',
        ),
    ]
