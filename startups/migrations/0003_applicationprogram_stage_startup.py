# Generated by Django 3.2.9 on 2022-10-08 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('startups', '0002_auto_20221008_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название программы')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Стадия разработки')),
            ],
            options={
                'verbose_name': 'Стадия разработки',
                'verbose_name_plural': 'Стадии разработки',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('website', models.CharField(max_length=600, verbose_name='Сайт стартапа')),
                ('description', models.TextField(verbose_name='Описание стартапа')),
                ('application_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startups.applicationprogram', verbose_name='Программа')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startups.stage', verbose_name='Стадия разработки')),
            ],
            options={
                'verbose_name': 'Стартап',
                'verbose_name_plural': 'Стартапы',
            },
        ),
    ]
