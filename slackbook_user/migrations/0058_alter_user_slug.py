# Generated by Django 3.2.18 on 2023-04-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0057_alter_chat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='id', max_length=200, unique=True),
        ),
    ]
