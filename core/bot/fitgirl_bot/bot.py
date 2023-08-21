from telebot import TeleBot
import markup
import messages
from DataBase import DataBase
from settings import TOKEN, DOWNLOAD_MEDIA_DIR
import traceback
from datetime import datetime

bot = TeleBot(TOKEN)

MEDIA_ROOT = str(DOWNLOAD_MEDIA_DIR)

@bot.message_handler(commands=['start'])
def commands_start(message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        name = message.from_user.first_name
        DataBase.set_new_user((message.from_user.id, message.from_user.username, message.from_user.first_name,
                               message.from_user.last_name, 'None', datetime.now()))
        DataBase.set_logging((user_id, f'Пользователь {name} нажал "start"', datetime.now()))
        bot.send_message(message.chat.id, text=messages.start_message, reply_markup=markup.gen_start_markup(),
                         parse_mode='HTML')


@bot.message_handler(regexp='✅ Найти по названию')
def regexp_find_by_name(message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        name = message.from_user.first_name
        DataBase.set_logging((user_id, f'Пользователь {name} нажал "✅ Найти по названию"', datetime.now()))

        def show_game(message):
            # print(message.text.encode('utf-8'))
            counter = 0
            games = DataBase.get_game_by_title(message.text)
            # print(str(games).encode('utf-8'))
            if games:
                DataBase.set_logging((user_id, f'Пользователь {name} ввёл в поиск "{message.text}" Найдено {str(len(games))} игр', datetime.now()))
                for game in games:
                    if counter == 10:
                        break
                    else:
                        try:
                            title = game['title']
                            image = game['image']
                            company = game['company']
                            languages = game['languages']
                            original_size = game['original_size']
                            repack_size = game['repack_size']
                            torrent_link_1337x = game['torrent_link_1337x']
                            torrent_link = game['torrent_link']
                            torrent_file = game['torrent_file']
                            _message = f'<b>{title}</b>' + \
                                       f'\nРазработчик: <code>{company}</code>' + \
                                       f'\nЯзык: <code>{languages}</code>' + \
                                       f'\nРазмер на диске: <code>{original_size}</code>' + \
                                       f'\nРазмер репака: <code>{repack_size}</code>\n' + \
                                       f'\n<b><a href="{torrent_link_1337x}">Скачать с сайта 1337x(нужен VPN)</a></b>\n' + \
                                       f'\n<b><a href="{torrent_link}">Скачать с fitgirl-repack</a></b>\n'
                            try:
                                bot.send_photo(message.chat.id, photo=open(MEDIA_ROOT+'/'+image, 'rb'),
                                               caption=_message, parse_mode='HTML',
                                               reply_markup=markup.gen_start_markup())
                            except:
                                print(traceback.format_exc())
                                bot.send_message(message.chat.id, text=_message, parse_mode='HTML',
                                                 reply_markup=markup.gen_start_markup())
                            try:
                                bot.send_document(message.chat.id, document=open(MEDIA_ROOT+'/'+torrent_file, 'rb'),
                                                  caption='Скачать .torrent файл')
                            except:
                                print(traceback.format_exc())
                            counter += 1
                        except:
                            print(traceback.format_exc())
            else:
                bot.send_message(message.chat.id, text=messages.no_result_by_title.format(message.text),
                                 reply_markup=markup.gen_start_markup())
                DataBase.set_logging((user_id, f'Пользователь {name} ввёл в поиск "{message.text}" Ничего не найдено', datetime.now()))

            print(message.text.encode('utf-8'))

        msg = bot.send_message(message.chat.id, text=messages.choose_by_title)
        bot.register_next_step_handler(msg, show_game)


@bot.message_handler(regexp='☎️ Связаться с администратором')
def regexp_call_admin(message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        name = message.from_user.first_name
        DataBase.set_logging((user_id, f'Пользователь {name} нажал "☎️ Связаться с администратором"', datetime.now()))
        bot.send_message(message.chat.id, text=messages.contact_admin, reply_markup=markup.gen_start_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query_handlers(call):
    print('OK')
    if call.message.chat.type == 'private':
        if 'link_from_channel' in call.data:
            user_id = call.message.from_user.id
            name = call.message.from_user.first_name
            DataBase.set_logging((user_id, f'Пользователь {name} перешёл в бота по ссылке из основного канала', datetime.now()))


bot.infinity_polling(skip_pending=False)
