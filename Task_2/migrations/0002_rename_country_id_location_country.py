# Generated by Django 4.1.3 on 2024-04-30 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task_2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='country_id',
            new_name='country',
        ),
    ]