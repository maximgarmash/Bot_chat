import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(constants.chat_id, "Response test 2")
# upd = bot.get_updates()
# last_upd = upd[-1]

@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.send_message(message.from_user.id, """ Мои возможности весьма специфичны.
    Но ты только посмотри! Все работает!!! """)
# message_from_user = last_upd.message
# print(message_from_user)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "а":
        bot.send_message(message.from_user.id, "Б")
    elif message.text == "б":
        bot.send_message(message.from_user.id, "В")
    else:
        bot.send_message(message.from_user.id, "Ты не умеешь играть в эту игру!!!")
    print(message)




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
