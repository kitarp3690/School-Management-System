# Generated by Django 5.0.3 on 2024-04-06 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0011_alter_attendence_report_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sms.staff'),
        ),
    ]