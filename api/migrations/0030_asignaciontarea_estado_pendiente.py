# Generated by Django 4.1.2 on 2022-10-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0029_asignaciontarea_asginacion"),
    ]

    operations = [
        migrations.AddField(
            model_name="asignaciontarea",
            name="estado_pendiente",
            field=models.CharField(
                choices=[("1", "activo"), ("0", "inactivo")], default="1", max_length=8
            ),
        ),
    ]
