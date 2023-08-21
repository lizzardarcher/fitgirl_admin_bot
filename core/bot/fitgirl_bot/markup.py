from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


def gen_start_markup():
    markup = ReplyKeyboardMarkup()
    buttonA = KeyboardButton('✅ Найти по названию')
    # buttonB = KeyboardButton('⭐️ Найти по жанру')
    buttonC = KeyboardButton('☎️ Связаться с администратором')
    # buttonD = KeyboardButton('🍕 Размещение рекламы')
    markup.row(
        buttonA,
        # buttonB
    )
    markup.row(
        buttonC,
        # buttonD
    )
    markup.resize_keyboard = True
    return markup


def gen_admin_start_markup():
    markup = ReplyKeyboardMarkup()
    buttonA = KeyboardButton('✅ Проверить посты')
    buttonB = KeyboardButton('🌇 Добавить город')
    buttonC = KeyboardButton('💬 Добавить канал')
    buttonD = KeyboardButton('⏱️ Время отложенной отправки')
    markup.row(buttonA, buttonD)
    markup.row(buttonB, buttonC)
    markup.resize_keyboard = True
    return markup


def gen_yes_no_markup(message_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes ✅", callback_data=f"cb_yes|{str(message_id)}"),
               InlineKeyboardButton("No ‼️", callback_data=f"cb_no|{str(message_id)}"), )
    return markup


def gen_message_links():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text="Скачать с помощью Бота ✅",
                                    callback_data="link_from_channel",
                                    url=f"https://t.me/fitgirlrepacktorrentbot",
                                    ))
    return markup