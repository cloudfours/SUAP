# Generated by Django 4.1.2 on 2022-10-28 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0022_alter_casos_id_comple_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casos",
            name="id_comple_info",
            field=models.OneToOneField(
                blank=True,
                db_column="id_comple_info",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.infocomplementaria",
            ),
        ),
        migrations.AlterField(
            model_name="casos",
            name="id_seguimiento",
            field=models.OneToOneField(
                db_column="id_seguimiento",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.seguimiento",
            ),
        ),
    ]
