# Generated by Django 5.0 on 2024-06-01 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("codigos", "0009_alter_codigo_data_codigo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="codigo",
            name="data_codigo",
            field=models.DateField(default=datetime.date(2024, 6, 1)),
        ),
    ]
