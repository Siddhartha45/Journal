# Generated by Django 5.0.3 on 2024-03-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0003_rename_cost_journal_estimated_cost_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="itinerary",
            name="day",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]