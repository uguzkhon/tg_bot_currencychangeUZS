import telebot, buttons, requests, json


bot = telebot.TeleBot('6116437158:AAEhdgh-htv-bETqQ7W5PZ97ePhyxbUYc7s')

bank_token = json.loads(requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').content)

amount = 0
usdRate = float(bank_token[0]['Rate'])
euroRate = float(bank_token[1]['Rate'])
rubRate = float(bank_token[3]['Rate'])



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome, type value')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Incorrect format')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        bot.send_message(message.chat.id, 'Choose valute', reply_markup= buttons.valute_buttons())

    else:
        bot.send_message(message.chat.id, 'Value should be more then 0!')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(lambda call: True)
def callback(call):
    if call.data == 'sum/eur':
        course = amount/euroRate
        bot.send_message(call.message.chat.id, f'Course rate: {round(course, 2)}. u can type another value')
        bot.register_next_step_handler(call.message, summa)

    elif call.data == 'sum/usd':
        course = amount / usdRate
        bot.send_message(call.message.chat.id, f'Course rate: {round(course, 2)}. u can type another value')
        bot.register_next_step_handler(call.message, summa)

    elif call.data == 'sum/rub':
        course = amount / rubRate
        bot.send_message(call.message.chat.id, f'Course rate: {round(course, 2)}. u can type another value')
        bot.register_next_step_handler(call.message, summa)
