# Generated by Django 4.2.7 on 2023-11-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_avaluos"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clienteid", models.IntegerField()),
                ("nombre", models.CharField(max_length=250)),
            ],
            options={"db_table": "jos_av_clientes", "managed": False,},
        ),
    ]