# Generated by Django 5.0 on 2024-04-26 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigos', '0007_alter_codigo_data_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo',
            name='data_codigo',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
    ]
