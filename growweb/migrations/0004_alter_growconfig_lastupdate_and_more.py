# Generated by Django 4.2.4 on 2023-08-16 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growweb', '0003_stage_remove_growconfig_stage_growconfig_stagetype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growconfig',
            name='lastUpdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='growconfighistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]