# Generated by Django 3.2.9 on 2022-10-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_startup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.TextField(unique=True, verbose_name='Название программы'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.TextField(unique=True, verbose_name='Стадия разработки'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(verbose_name='Описание стартапа'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='name',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='presentation',
            field=models.TextField(verbose_name='Презентация'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='website',
            field=models.TextField(verbose_name='Сайт стартапа'),
        ),
    ]
