# Generated by Django 4.1.5 on 2023-01-06 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0004_vehicleorder_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicleorder",
            name="owner",
        ),
    ]
