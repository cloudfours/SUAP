# Generated by Django 4.1.2 on 2022-11-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0035_alter_casos_adjunto_seg_alter_casos_adjunto_terc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casos",
            name="adjunto_seg",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="casos",
            name="adjunto_terc",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="casos",
            name="formula_medica",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
