# Generated by Django 4.2.2 on 2023-06-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_channel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='game',
            name='torrent_link',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Ссылка на торрент-файл'),
        ),
        migrations.AlterField(
            model_name='game',
            name='torrent_link_1337x',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Ссылка на торрент-файл 1337x'),
        ),
        migrations.AlterField(
            model_name='game',
            name='torrent_link_magnet',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Ссылка на торрент-файл magnet'),
        ),
    ]
