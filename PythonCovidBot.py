import telebot
from telebot import types
import COVID19Py
import requests

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1414591926:AAGan1P0YxfHNcbk2hAALP1icrDAuGjC_g0')


# Функция, которая сработает, когда пользовтель отправит /start, затем, создаются 4 кнопки с названиями некоторых городов и приветствие
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Москва')
    btn2 = types.KeyboardButton('Санкт-Петербург')
    btn3 = types.KeyboardButton('Дагестан')
    btn4 = types.KeyboardButton('Севастополь')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nЧтобы получить последнюю информацию по числу случаев заражения коронавирусом " \
                   f"напишите название города, края или области, например: Москва, Иркутская область, Пермский край и т.д.\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


# Функция, которая сработает при отправке города/края/области боту

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "москва":
        location = "Москва"
    elif get_message_bot == "санкт-петербург":
        location = "Санкт-Петербург"
    elif get_message_bot == "дагестан":
        location = "Дагестан"
    elif get_message_bot == "севастополь":
        location = "Севастополь"
    elif get_message_bot == "московская область":
        location = "Московская область"
    elif get_message_bot == "удмуртия":
        location = "Удмуртия"
    elif get_message_bot == "татарстан":
        location = "Татарстан"
    elif get_message_bot == "мордовия":
        location = "Мордовия"
    elif get_message_bot == "чечня":
        location = "Чечня"
    elif get_message_bot == "ульяновская область":
        location = "Ульяновская область"
    elif get_message_bot == "саратовская область":
        location = "Саратовская область"
    elif get_message_bot == "самарская область":
        location = "Самарская область"
    elif get_message_bot == "башкортостан":
        location = "Башкортостан"
    elif get_message_bot == "пермский край":
        location = "Пермский край"
    elif get_message_bot == "пензенская область":
        location = "Пензенская область"
    elif get_message_bot == "оренбургская область":
        location = "Оренбургская область"
    elif get_message_bot == "нижегородская область":
        location = "Нижегородская область"
    elif get_message_bot == "марий Эл":
        location = "Марий Эл"
    elif get_message_bot == "кировская область":
        location = "Кировская область"
    elif get_message_bot == "ставропольский край":
        location = "Ставропольский край"
    elif get_message_bot == "ростовская область":
        location = "Ростовская область"
    elif get_message_bot == "северная осетия":
        location = "Северная Осетия"
    elif get_message_bot == "чувашия":
        location = "Чувашия"
    elif get_message_bot == "свердловская область":
        location = "Свердловская область"
    elif get_message_bot == "калмыкия":
        location = "Калмыкия"
    elif get_message_bot == "ингушетия":
        location = "Ингушетия"
    elif get_message_bot == "тыва":
        location = "Тыва"
    elif get_message_bot == "крым":
        location = "Крым"
    elif get_message_bot == "ненецкий автономный округ":
        location = "Ненецкий автономный округ"
    elif get_message_bot == "адыгея":
        location = "Адыгея"
    elif get_message_bot == "карелия":
        location = "Карелия"
    elif get_message_bot == "мурманская область":
        location = "Мурманская область"

    # Информация берется с ресурса стопкоронавирус.рф, парсится и записывается в определенные переменные, чтобы затем вывести
    data = requests.get("https://covid19.rosminzdrav.ru/wp-json/api/mapdata/").json()

    for city in data['Items']:
        if city['LocationName'] == location:
            print(city['Confirmed'], city['Recovered'], city['Deaths'],
                  city['Confirmed'] - city['Deaths'] - city['Recovered'])
            confirmed = city['Confirmed']
            recovered = city['Recovered']
            deaths = city['Deaths']
            sick = city['Confirmed'] - city['Deaths'] - city['Recovered']
            print(deaths)
            print(type(deaths))
            bot.send_message(message.chat.id, 'Всего случаев заражения: ')
            bot.send_message(message.chat.id, confirmed)
            bot.send_message(message.chat.id, 'Больны сейчас: ')
            bot.send_message(message.chat.id, sick)
            bot.send_message(message.chat.id, 'Выздоровело: ')
            bot.send_message(message.chat.id, recovered)
            bot.send_message(message.chat.id, 'Смертей: ')
            bot.send_message(message.chat.id, deaths)


# Бот будет работать всегда
bot.polling(none_stop=True)
