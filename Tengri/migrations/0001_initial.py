# Generated by Django 5.0.2 on 2024-04-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=200)),
                ("authors", models.CharField(max_length=20000)),
                ("main_text", models.TextField()),
                ("main_link", models.CharField(max_length=200)),
                ("project_date", models.DateTimeField()),
                ("project_logo", models.CharField(max_length=200)),
                ("project_tags", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
