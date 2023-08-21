from core.bot.fitgirl_bot.DataBase import DataBase

val = 'deluxe'
g = DataBase.get_game_by_title(val)
for i in g:
    print(i['title'])
