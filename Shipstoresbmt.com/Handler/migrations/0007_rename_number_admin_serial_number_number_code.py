# Generated by Django 4.0.5 on 2022-07-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0006_admin_serial_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_serial_number',
            old_name='Number',
            new_name='Number_code',
        ),
    ]