# Generated by Django 4.1.5 on 2023-01-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myvotingapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Count",
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
                ("like_count", models.IntegerField(default=0)),
                ("dislike_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(name="votes",),
    ]
