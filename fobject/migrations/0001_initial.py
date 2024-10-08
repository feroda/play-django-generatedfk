# Generated by Django 5.1.dev20240328164504 on 2024-04-11 11:42

import django.db.models.deletion
import django.db.models.functions.comparison
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('last_updated_by_id', models.GeneratedField(db_index=True, db_persist=True, expression=django.db.models.functions.comparison.Greatest('created_by', 'confirmed_by', 'canceled_by'), output_field=models.BigIntegerField())),
                ('canceled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='canceled_xevents_set', to=settings.AUTH_USER_MODEL)),
                ('confirmed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmed_xevents_set', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_xevents_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
