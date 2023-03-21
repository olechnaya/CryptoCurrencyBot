import json
import requests

import telebot

TOKEN = '6091943863:AAFubE3amsd38QZMJaGSKzVxrg2CBRx1GU4'

keys = {
    'биткоин':'BTC',
    'эфириум':'ETH',
    'доллар': 'USD'
}

#one line
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу с валютой нужно ввести команду в чате:\n<имя валюты> \
<в какую валюту перевести> \
<какое количество нужно переввести>\
Увидеть список всех доступных валют: <curr>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['curr'])
def available_currencies(message: telebot.types.Message):
    text = 'Доступные валюты:'

    for k in keys:
        text = '\n'.join((text, k))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    from_, to_, amount_ = message.text.split(' ')

    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[from_]}&tsyms={keys[to_]}")

    # if json.loads(r.content)["Response"] and json.loads(r.content)["Response"] == "Error":
    #     text = "Система не может перевести указанную валюту. Еще раз ознакомьтесь со списком конвертируемых валют, введя команду /curr"

    answer_to_user = json.loads(r.content)[keys[to_]]

    text = f'Цена {amount_} {from_} в {to_}: {int(answer_to_user)*int(amount_)}'
    bot.send_message(message.chat.id, text)


bot.polling()