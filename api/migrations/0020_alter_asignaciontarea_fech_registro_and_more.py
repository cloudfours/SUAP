# Generated by Django 4.1.2 on 2022-10-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_alter_asignaciontarea_fecha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asignaciontarea",
            name="fech_registro",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="asignaciontarea", name="fecha", field=models.DateTimeField(),
        ),
    ]
