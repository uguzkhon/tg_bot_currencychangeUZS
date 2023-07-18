from telebot import types

def valute_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton('SUM/EUR', callback_data='sum/eur')
    btn2 = types.InlineKeyboardButton('SUM/USD', callback_data='sum/usd')
    btn3 = types.InlineKeyboardButton('SUM/RUB', callback_data='sum/rub')

    kb.add(btn1, btn2, btn3)
    return kb