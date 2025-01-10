# Generated by Django 5.1 on 2025-01-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0031_staff_subject_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='staff',
            name='subjects',
            field=models.ManyToManyField(related_name='staff_members', to='sms.subject'),
        ),
    ]
