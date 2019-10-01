import telebot
import random
import os
import constants
bot = telebot.TeleBot(constants.token)

# bot.send_message(constants.chat_id, "Response test 2")
# upd =requests.get(constants.url+constants.token + '/getupdates')
# last_upd = upd[-1]
# print(last_upd.message.message_id)
# print(type(upd.json()))
print(bot.get_me())

def log(message,answer):
    print("\n --------")
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
        directory = 'D:/Python/Projects/Bot/photo'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'аудио':
        directory = 'D:/Python/Projects/Bot/audio'
        audio = open(directory + '/' + 'muzlome_Tima_Belorusskikh_-_Mokrye_krossy_58229891.mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text ==


    else:
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    # print(message)





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

