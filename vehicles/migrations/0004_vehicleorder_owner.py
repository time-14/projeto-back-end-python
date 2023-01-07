# Generated by Django 4.1.5 on 2023-01-06 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vehicles", "0003_remove_vehicleorder_owner_vehicleorder_vehicle"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicleorder",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner_order",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
