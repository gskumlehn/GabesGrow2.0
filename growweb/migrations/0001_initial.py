# Generated by Django 4.2.4 on 2023-08-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]