# Generated by Django 4.1.1 on 2022-09-20 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Countries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="People",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_mame", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="countries",
                        to="fbv.countries",
                    ),
                ),
            ],
        ),
    ]
