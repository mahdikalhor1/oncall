# Generated by Django 4.2.15 on 2024-10-09 18:39

from django.db import migrations
import django_migration_linter as linter


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0060_relatedincident'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.RemoveField(
            model_name='alertgroup',
            name='resolved_by_alert',
        ),
    ]
