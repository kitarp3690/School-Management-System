# Generated by Django 5.1 on 2025-01-08 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0025_remove_student_batch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='sms.batch'),
            preserve_default=False,
        ),
    ]
