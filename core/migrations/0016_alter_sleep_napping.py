# Generated by Django 3.2.9 on 2021-11-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_add_nap_field_for_sleep"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sleep",
            name="napping",
            field=models.BooleanField(
                editable=False, null=True, verbose_name="Napping"
            ),
        ),
    ]
