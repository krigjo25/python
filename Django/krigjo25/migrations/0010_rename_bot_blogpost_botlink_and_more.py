# Generated by Django 4.0.4 on 2022-05-10 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krigjo25', '0009_rename_link_blogpost_bot_blogpost_readme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='bot',
            new_name='botlink',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='readme',
            new_name='readmelink',
        ),
    ]
