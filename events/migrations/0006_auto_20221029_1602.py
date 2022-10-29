# Generated by Django 3.2.16 on 2022-10-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_add_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='add_information',
            field=models.TextField(default='additional information', verbose_name='Дополнительное описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.TextField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='event',
            name='theme',
            field=models.TextField(verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TextField(verbose_name='Время'),
        ),
    ]