from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


class Game(models.Model):
    title = models.CharField(max_length=1000, unique=True, null=True, blank=True, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    genre = models.CharField(max_length=4000, null=True, blank=True, verbose_name='Жанр')
    description = models.TextField(max_length=4000, null=True, blank=True, verbose_name='Описание')
    company = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Издатель')
    languages = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Поддерживаемые Языки')
    original_size = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Размер после установки')
    repack_size = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Размер репака')
    torrent_link_1337x = models.CharField(max_length=4000, null=True, blank=True, verbose_name='Ссылка на торрент-файл 1337x')
    torrent_link_magnet = models.CharField(max_length=4000, null=True, blank=True, verbose_name='Ссылка на торрент-файл magnet')
    torrent_link = models.CharField(max_length=4000, null=True, blank=True, verbose_name='Ссылка на торрент-файл')
    torrent_file = models.FileField(null=True, blank=True, verbose_name='Торрент-файл')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        # ordering = ['-date']

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img src="/media/%s" width="40" heigth="40"/>' % escape(self.image))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True


class Genre(models.Model):
    tag = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Тэг')
    id = models.AutoField(primary_key=True, editable=False)


class User(models.Model):
    id = models.IntegerField(null=False, blank=True, primary_key=True, verbose_name='Id', editable=False)
    username = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Username')
    first_name = models.CharField(null=True, blank=True, max_length=1000, verbose_name='First_name')
    last_name = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Last_name')
    phone_number = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Phone_number')
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name) + ' ' + str(self.id)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Channel(models.Model):
    id = models.IntegerField(auto_created=True, null=False, blank=True, primary_key=True, verbose_name='Id', editable=False)
    channel = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Канал')
    title = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Название Канала')

    def __str__(self):
        return str(self.channel)

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class Logging(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    entry = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Запись')
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.date) + ' | ' + str(self.entry)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'