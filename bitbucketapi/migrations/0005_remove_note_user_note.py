# Generated by Django 3.2.6 on 2021-08-23 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bitbucketapi", "0004_note_user_note"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="user_note",
        ),
    ]
