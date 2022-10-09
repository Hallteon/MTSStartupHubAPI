# Generated by Django 3.2.9 on 2022-10-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Платформа',
                'verbose_name_plural': 'Платформы',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=3000, verbose_name='Описание')),
                ('goals', models.CharField(max_length=500, verbose_name='Цели')),
                ('equipment', models.CharField(max_length=250, verbose_name='Оборудование')),
                ('date', models.CharField(max_length=60, verbose_name='Дата')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.platform', verbose_name='Платформа')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
