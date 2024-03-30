# Generated by Django 5.1.dev20240328164504 on 2024-03-30 13:06

import django.db.models.functions.comparison
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noopfk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_updated_by_id',
            field=models.GeneratedField(db_index=True, db_persist=True, expression=django.db.models.functions.comparison.Greatest('created_by', 'confirmed_by', 'canceled_by'), output_field=models.BigIntegerField()),
        ),
    ]