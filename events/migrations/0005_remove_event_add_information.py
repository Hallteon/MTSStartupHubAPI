# Generated by Django 3.2.16 on 2022-10-29 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_add_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='add_information',
        ),
    ]