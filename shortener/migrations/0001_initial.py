# Generated by Django 4.0.3 on 2022-08-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UrlShortener",
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
                ("url", models.URLField()),
                (
                    "shortcode",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                ("count", models.IntegerField(default=0)),
            ],
        )
    ]
