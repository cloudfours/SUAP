# Generated by Django 4.1.2 on 2022-10-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_alter_infocomplementaria_clasificacion_pbs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="terapia",
            name="id_terapia",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
