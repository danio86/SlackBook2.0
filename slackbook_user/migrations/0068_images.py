# Generated by Django 3.2.18 on 2023-04-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0067_alter_chat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('def_avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
