# Generated by Django 4.2.7 on 2023-11-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_estatus_alter_valuadores_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Estado",
            fields=[
                ("estadoid", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=250)),
                ("clave", models.CharField(max_length=10)),
            ],
            options={"db_table": "jos_estados", "managed": False,},
        ),
    ]
