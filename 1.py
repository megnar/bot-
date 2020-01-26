import telebot;
bot = telebot.TeleBot('854681764:AAFJQ3_DPmvOc_kioH9tRiZ-LUwagABKzho');


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ты Рома', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text.lower() == "/love":
        bot.send_message(message.from_user.id, "для Ромочки:3")
        bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAMMXizHKNJoLY4oHk1wn2A9q9JSpUgAAgEAA4rWmzhPSMHTaNLd5xgE")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /love")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling()














