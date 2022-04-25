# Generated by Django 2.2 on 2019-05-17 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_auto_20190502_1701"),
    ]

    operations = [
        migrations.CreateModel(
            name="Temperature",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temperature", models.FloatField(verbose_name="Temperature")),
                ("time", models.DateTimeField(verbose_name="Time")),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="temperature",
                        to="core.Child",
                        verbose_name="Child",
                    ),
                ),
            ],
            options={
                "verbose_name": "Temperature",
                "verbose_name_plural": "Temperature",
                "ordering": ["-time"],
                "default_permissions": ("view", "add", "change", "delete"),
            },
        ),
    ]
