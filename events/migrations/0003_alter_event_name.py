# Generated by Django 3.2.9 on 2022-10-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
