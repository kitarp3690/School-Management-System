# Generated by Django 5.1 on 2025-01-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0040_rename_attendence_attendance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendence_date',
            new_name='attendance_date',
        ),
        migrations.RenameField(
            model_name='attendance_report',
            old_name='attendence_id',
            new_name='attendance_id',
        ),
    ]
