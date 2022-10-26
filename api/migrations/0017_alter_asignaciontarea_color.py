# Generated by Django 4.1.2 on 2022-10-26 23:20

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_asignaciontarea_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asignaciontarea",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF",
                image_field=None,
                max_length=18,
                samples=[("#FFFFFF", "white"), ("#000000", "black")],
            ),
        ),
    ]