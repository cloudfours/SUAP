# Generated by Django 4.1.2 on 2022-10-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0026_alter_infocomplementaria_fech_rad_aut_farm_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="infocomplementaria",
            name="fech_rad_for_eps",
            field=models.DateTimeField(
                blank=True, db_column="fech_rad_for_EPS", null=True
            ),
        ),
    ]
