# Generated by Django 4.1.2 on 2022-10-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_alter_gestorfarmacia_id_far"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casos",
            name="estado_pendiente",
            field=models.CharField(
                choices=[("1", "activo"), ("0", "inactivo")], default="1", max_length=8
            ),
        ),
    ]