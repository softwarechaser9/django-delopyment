# Generated by Django 4.0.1 on 2022-01-09 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0002_likes_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
