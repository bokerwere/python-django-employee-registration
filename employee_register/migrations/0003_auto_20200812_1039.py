# Generated by Django 3.0.8 on 2020-08-12 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_auto_20200808_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='mopile',
            new_name='mobile',
        ),
    ]
