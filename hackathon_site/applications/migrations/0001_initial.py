# Generated by Django 3.0.5 on 2020-05-07 20:06

import applications.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "team_code",
                    models.CharField(
                        default=applications.models._generate_team_code, max_length=5
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("preferred_name", models.CharField(max_length=255)),
                ("birthday", models.DateField()),
                ("gender", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=20)),
                ("resume", models.FileField(upload_to="applications/resumes/")),
                ("q1", models.TextField()),
                ("q2", models.TextField()),
                ("q3", models.TextField()),
                ("mlh_conduct_agree", models.BooleanField(default=False)),
                ("mlh_data_agree", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applications.Team",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
