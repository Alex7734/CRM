# Generated by Django 4.1.1 on 2022-09-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0002_rename_modified_lead_modified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("contacted", "Contacted"),
                    ("inprogress", "In progress"),
                    ("lost", "Lost"),
                    ("won", "Won"),
                ],
                default="new",
                max_length=25,
            ),
        ),
    ]
