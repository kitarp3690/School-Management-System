# Generated by Django 5.0.3 on 2024-04-06 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0014_alter_subject_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='staff',
        ),
    ]
