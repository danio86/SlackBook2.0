# Generated by Django 3.2.18 on 2023-04-01 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0014_channel_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='privat',
        ),
    ]
