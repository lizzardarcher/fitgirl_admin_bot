from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

from bot.models import Game, Genre, User, Channel, Logging


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'company', 'languages')
    list_display_links = ('title',)
    # list_filter = ['company']
    search_fields = ('title',)
    search_help_text = 'Поиск'
    fields = [('image_tag'),
              'description',
              ('company', 'languages', 'original_size', 'repack_size'),
              ('torrent_link_1337x', 'torrent_link_magnet', 'torrent_link'),
              'torrent_file']
    readonly_fields = ['title', 'image_tag']

class LoggingAdmin(admin.ModelAdmin):

    def time_seconds(self, obj):
        return obj.date.strftime("%d %b %Y %H:%M:%S")

    time_seconds.admin_order_field = 'date'
    time_seconds.short_description = 'Precise Time'

    list_display = ('time_seconds', 'entry')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'date')
    list_display_links = ('username', 'first_name', 'last_name')
    # list_filter = ['company']
    search_fields = ('username',)
    search_help_text = 'Поиск'
    fields = ['username', 'first_name', 'last_name', 'phone_number']


admin.site.register(Game, GameAdmin)
admin.site.register(Logging, LoggingAdmin)
admin.site.register(User, UserAdmin)
# admin.site.register(Genre)
admin.site.register(Channel)
