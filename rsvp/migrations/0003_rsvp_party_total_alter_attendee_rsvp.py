# Generated by Django 5.0.1 on 2024-01-07 04:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_remove_rsvp_attendees_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='party_total',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='rsvp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='rsvp.rsvp'),
        ),
    ]
