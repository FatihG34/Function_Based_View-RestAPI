# Generated by Django 4.1.1 on 2022-09-20 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fbv", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="people",
            old_name="first_mame",
            new_name="first_name",
        ),
    ]
