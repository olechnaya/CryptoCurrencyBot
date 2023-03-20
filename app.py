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
    bot.reply_to(message, text)

bot.polling()