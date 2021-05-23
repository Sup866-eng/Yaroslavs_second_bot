import telebot

bot = telebot.TeleBot("1703691430:AAF8nF6mM089IR53BFrByM1v9vp8h1-Vwvc")

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row("Привет", "Пока")
keybord2 = telebot.types.ReplyKeyboardMarkup(True)
keybord2.row("Youtube", "Twitter", "Tiktok", "VK")
keybord2.row("Facebook", "Instagramm")

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, "Привет, давай начнём общаться", reply_markup=keybord1)

@bot.message_handler(content_types=['text'])

def send_text(message):
    message.text = message.text.lower()
    if message.text == "привет":
        bot.send_message(message.chat.id, "И тебе привет!")
        bot.send_message(message.chat.id, "Какая твоя любимая соцсеть?", reply_markup=keybord2)
    if message.text == "пока":
        bot.send_message(message.chat.id, "И тебе пока!")
    if message.text == "youtube":
        bot.send_message(message.chat.id, "Мне нравится смотреть Ютьюб!")
    if message.text == "twitter":
        bot.send_message(message.chat.id, "У меня нет Твитера :(")
    if message.text == "tiktok":
        bot.send_message(message.chat.id, "В тиктоке смешные видео :)")
    if message.text == "vk":
        bot.send_message(message.chat.id, "Я иногда захожу в ВК!")
    if message.text == "facebook":
        bot.send_message(message.chat.id, "У меня нет Фейсбука :(")
    if message.text == "instagramm":
        bot.send_message(message.chat.id, "Я иногда смотрю сторис в инстаграмме")

bot.polling()