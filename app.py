import telebot
from config import keys, TOKEN
from utils import CryptoConverter,APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу с валютой нужно ввести команду в чате:\n<имя валюты> \
<в какую валюту перевести> \
<какое количество нужно переввести>\
Увидеть список всех доступных валют: <curr>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def available_currencies(message: telebot.types.Message):
    text = 'Доступные валюты:'

    for k in keys:
        text = '\n'.join((text, k))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        # создали отдельную переменную чтобы отлавливать некорректно введенные данные
        user_input = message.text.split(' ')

        if len(user_input) < 3:
            raise APIException('Мало параметров')
        elif len(user_input) > 3:
            raise APIException('Много параметров')

        from_, to_, amount_ = user_input
        answer_to_user = CryptoConverter.convert(from_, to_, amount_)

    except APIException as e:
        bot.reply_to(message, f"Ошибка ввода пользователем:\n  - {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f'Цена {amount_} {from_} в {to_}: {float(answer_to_user)*float(amount_)}'
        bot.send_message(message.chat.id, text)


bot.polling()