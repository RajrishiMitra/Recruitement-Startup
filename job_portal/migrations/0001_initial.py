# Generated by Django 4.2.4 on 2023-08-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobPosting",
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
                ("job_title", models.CharField(max_length=100)),
                ("job_category", models.CharField(max_length=50)),
                ("job_description", models.TextField()),
                ("job_location", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=254)),
            ],
        ),
    ]
