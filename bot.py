import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(constants.chat_id, "Response test 2")
upd = bot.get_updates()
print(upd)