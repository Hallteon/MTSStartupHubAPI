# Generated by Django 3.2.9 on 2022-10-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='theme',
            field=models.TextField(default='standart', verbose_name='Тема'),
        ),
    ]