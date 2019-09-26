import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(constants.chat_id, "Response test 2")
upd = bot.get_updates()
# last_upd = upd[-1]
# print(last_upd.message.message_id)
# print(bot.get_me())

def log(message, answer):
    print("\n ------------------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print("Ответ -", answer)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.send_message(message.from_user.id, """ Мои возможности весьма специфичны.
    Но ты только посмотри! Все работает!!! """)
# message_from_user = last_upd.message
# print(message_from_user)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты не умеешь играть в эту игру :("
    if message.text == "а":
        answer = "Б"
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    elif message.text == "б":
        answer = "В"
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    elif message.text == 'фото':
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, constants.file_not_bad)
    # elif message.text == 'get updates':


    else:
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    # print(message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.from_user.id, message.photo.file_id)




#
# @bot.message_handler(content_types=['commands'])
# def handle_command(message):
#     print("Пришла команда")
#
#
# @bot.message_handler(content_types=['sticker'])
# def handle_sticker(message):
#     print("Пришел стикер")


bot.polling(none_stop=True, interval=0)

