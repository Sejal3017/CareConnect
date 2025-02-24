# Generated by Django 4.1.7 on 2023-04-05 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_insurance_plans"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor_rating",
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
                ("comments", models.TextField()),
                (
                    "ratings",
                    models.IntegerField(
                        choices=[
                            ("1", "Worst"),
                            ("2", "Bad"),
                            ("3", "Average"),
                            ("4", "Good"),
                            ("5", "Excellent"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "d_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.doctor"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Doctor Ratings",
            },
        ),
    ]
