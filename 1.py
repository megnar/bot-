import telebot;
import sqlite3;
from telebot import apihelper
PROXY = 'socks5://54.38.195.161:53047'
apihelper.proxy = {'https': PROXY}
bot = telebot.TeleBot('854681764:AAFJQ3_DPmvOc_kioH9tRiZ-LUwagABKzho');
def drop():
    conn = sqlite3.connect(r"C:\Users\Megnar\gays\mydatabase.db") # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    
    cursor.execute("""DROP TABLE  IF EXISTS albums""")

    cursor.execute("""CREATE TABLE albums(
                    id INTEGER PRIMARY KEY,
                    message STRING NOT NULL,
                    id_chelbusa INTEGER NOT NULL
                    )
                   """)    
        

def pisechka(message, id_c):

    conn = sqlite3.connect(r"C:\Users\Megnar\gays\mydatabase.db") # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
     
    # Создание таблицы


    cursor.execute("""insert into albums (message, id_chelbusa) values ( ?, ?)""", ( message,  id_c))


    # Сохраняем изменения
    conn.commit()
def read():
    conn = sqlite3.connect(r"C:\Users\Megnar\gays\mydatabase.db") # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
     
    
    cursor.execute('SELECT count(*) FROM albums')

    (res, )  = cursor.fetchone()
    print (res)
    for row in cursor.execute("select * from albums"):
        print(row)   

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/love', '/fap')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    pisechka(message.text, message.from_user.id)
    if message.text.lower() == "/love":
        bot.send_message(message.from_user.id, "для Ромочки:3")
        bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAMMXizHKNJoLY4oHk1wn2A9q9JSpUgAAgEAA4rWmzhPSMHTaNLd5xgE")
    elif message.text == "/fap":
        keyboard2 = telebot.types.ReplyKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text = 'чисто подрунькать', url = "https://yandex.by")
        keyboard2.add(url_button)
        bot.send_message(message.chat.id, 'Ну нихуя себе', reply_markup=keyboard2)
        #bot.send_message(message.from_user.id, "Напиши /love")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, """Есть несколько функций например
                                                /fap
                                                /love""")

    elif message.text == "чисто подрунькать":
        bot.send_message(message.from_user.id, "сорян в доработке")
    
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling()

