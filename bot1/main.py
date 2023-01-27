import telebot
import cv2
from telebot import types
import qrcode
import time
import requests





bot = telebot.TeleBot('5628853718:AAGn0IP8sp4aieBO8FskptIiihaaGuT7qxE')


@bot.message_handler(commands=['start'])
def parking (message):
    mess = f'Здравствуйте <b>{message.from_user.first_name}</b> '
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, f"<i><b>Вас приветствует сервис автоматизированной парковки Smart Parking 🅿️</b></i>",
                     parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    yes = types.KeyboardButton('Да✅')
    NON = types.KeyboardButton('Нет❌')
    markup.add(yes,NON)
    bot.send_message(message.chat.id, f"Ваш город это:" f"<i><b> Ижевск ?</b></i>", parse_mode='html', reply_markup=markup)





    @bot.message_handler(content_types=['text'])
    def func(message):
        global markup
        if (message.text == "Да✅"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        elif ("Нет❌" == message.text):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bt1 = types.KeyboardButton("Ижевск")
            bt2 = types.KeyboardButton("Москва")
            bt3 = types.KeyboardButton("Санкт-Петербург")
            bt4 = types.KeyboardButton("Новосибирск")
            bt6 = types.KeyboardButton("Сочи")
            bt7 = types.KeyboardButton("Мурманск")
            bt8 = types.KeyboardButton("Екатеринбург")
            bt5 = types.KeyboardButton("Нижний Новгород")
            bt9 = types.KeyboardButton("Калининград")
            markup.add(bt1, bt2, bt3, bt4,bt5,bt6,bt7,bt8,bt9)
            bot.send_message(message.chat.id, text="Выберите свой город:", reply_markup=markup)


        if (message.text == "Москва"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Ижевск"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Мурманск"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Сочи"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Калининград"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)


        if (message.text == "Новосибирск"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Нижний Новгород"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Екатеринбург"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Санкт-Петербург"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Настройки местоположения применены✅", reply_markup=markup)
            bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

        if (message.text == "Контакты📬"):
            bot.send_message(message.chat.id, text="Техподдержка: @shadowlady69")

        
        if (message.text == "Поиск парковки🔎"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True,)
            geo = types.KeyboardButton(text='Предоставть доступ✅', request_location=True)
            back = types.KeyboardButton('Вернуться в главное меню↩')
            markup.add(geo,back)
            bot.send_message(message.chat.id, text="Для продолжения необходимо разрешить доступ к своему местоположению", reply_markup=markup)
            time.sleep(7)
            bot.send_message(message.chat.id, f"<i><b>Рядом с вами найдено 3 парковки ✅</b></i>", parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, f"1)ТРЦ Италмас, улица Ленина 69, 90 метров от вас", parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, f"2)ГСК №5, улица Бабушкина 37, 320 метров от вас", parse_mode='html',reply_markup=markup)
            bot.send_message(message.chat.id, f"3)АЗС Газпром, улица Пушкина 112, 540 метров от вас", parse_mode='html',reply_markup=markup)
            link = "http://icanhazip.com/"
            responce = requests.get(link).text
            bot.send_message(message.chat.id,responce,reply_markup=markup)
            geo = types.ReplyKeyboardMarkup()
            back = types.ReplyKeyboardMarkup()


        if (message.text == "Я уже на парковке👋"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            qrr = types.KeyboardButton(text='Сканировать Qr Code')
            hanf = types.KeyboardButton(text='Выбрать парковку вручную')
            back = types.KeyboardButton('Вернуться в главное меню↩')
            markup.add(hanf,qrr, back)
            bot.send_message(message.chat.id, text='Выберите действие:', reply_markup=markup)

        if (message.text == "Сканировать Qr Code"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True,)
            bot.send_message(message.chat.id,text="Пожалуйста, пришлите этому боту номер парковки, указанный на информационном "
                                                  "стенде рядом с ней",reply_markup=markup)
            bot.send_message(message.chat.id, f"<i><b>Пример:</b></i>", parse_mode='html',
                             reply_markup=markup)
            chatId = message.chat.id
            p = open ("number.png", 'rb')
            bot.send_photo(chatId, p)

        if (message.text == "Выбрать парковку вручную"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            p1 = types.KeyboardButton(text='ЖК "Настроение"')
            p2 = types.KeyboardButton(text='ТРК "Петровский"')
            p3 = types.KeyboardButton(text='Пригородный ЖД Вокзал')
            p4 = types.KeyboardButton(text='"Аэропорт"')
            back = types.KeyboardButton('Вернуться в главное меню↩')
            markup.add(p1, p2, p3,p4,back)
            bot.send_message(message.chat.id, text='Выберите действие:', reply_markup=markup)






        if (message.text == "Настройки⚙"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            city = types.KeyboardButton(text='Изменить город')
            lang = types.KeyboardButton(text='Сменить язык')
            back = types.KeyboardButton('Вернуться в главное меню↩')
            markup.add(city, lang, back)
            bot.send_message(message.chat.id, text='Выберите действие:', reply_markup=markup)


        if (message.text == "Изменить город"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bt1 = types.KeyboardButton("Ижевск")
            bt2 = types.KeyboardButton("Москва")
            bt3 = types.KeyboardButton("Санкт-Петербург")
            bt4 = types.KeyboardButton("Новосибирск")
            bt6 = types.KeyboardButton("Сочи")
            bt7 = types.KeyboardButton("Мурманск")
            bt8 = types.KeyboardButton("Екатеринбург")
            bt5 = types.KeyboardButton("Нижний Новгород")
            bt9 = types.KeyboardButton("Калининград")
            markup.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9)
            bot.send_message(message.chat.id, text="Выберите свой город:", reply_markup=markup)

        if (message.text == "Сменить язык"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ln1 = types.KeyboardButton("Русский")
            ln2 = types.KeyboardButton("English")
            ln3 = types.KeyboardButton("中國人")
            markup.add(ln1, ln2, ln3)
            bot.send_message(message.chat.id, text="Выберите язык:", reply_markup=markup)


        elif (message.text == "Вернуться в главное меню↩"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            qr = types.KeyboardButton(text='Я уже на парковке👋')
            start = types.KeyboardButton('Поиск парковки🔎')
            contacts = types.KeyboardButton('Контакты📬')
            setting = types.KeyboardButton('Настройки⚙')
            markup.add(start, qr, setting, contacts)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
bot.polling(none_stop=True)