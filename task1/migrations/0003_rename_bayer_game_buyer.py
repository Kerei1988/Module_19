# Generated by Django 5.1 on 2024-08-11 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_rename_bayer_buyer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='bayer',
            new_name='buyer',
        ),
    ]
