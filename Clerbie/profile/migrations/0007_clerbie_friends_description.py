# Generated by Django 5.1.4 on 2025-01-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_clerbie_friends_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='clerbie_friends',
            name='description',
            field=models.TextField(blank=True, max_length=7000, null=True),
        ),
    ]
