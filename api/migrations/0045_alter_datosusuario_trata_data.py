# Generated by Django 4.1.2 on 2022-11-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0044_alter_datosusuario_trata_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datosusuario",
            name="trata_data",
            field=models.CharField(
                choices=[
                    (
                        1,
                        "Acepto Términos y condiciones y autorizacion de tratamiento de datos",
                    )
                ],
                default=None,
                max_length=30,
                null=True,
            ),
        ),
    ]
