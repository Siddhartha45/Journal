# Generated by Django 5.0.3 on 2024-03-21 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0005_itinerary_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="JournalImages",
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
                ("journal_photo", models.ImageField(upload_to="")),
                (
                    "journal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="journal.journal",
                    ),
                ),
            ],
        ),
    ]
