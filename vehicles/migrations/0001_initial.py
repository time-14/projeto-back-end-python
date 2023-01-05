# Generated by Django 4.1.5 on 2023-01-05 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("brand", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("year", models.CharField(max_length=4)),
                ("unique_owner", models.BooleanField(default=False)),
                ("price", models.PositiveIntegerField()),
                ("mileage", models.CharField(max_length=8)),
                (
                    "description",
                    models.CharField(default=None, max_length=256, null=True),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
