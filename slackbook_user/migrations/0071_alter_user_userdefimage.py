# Generated by Django 3.2.18 on 2023-04-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0070_alter_user_userdefimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userDefImage',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]
