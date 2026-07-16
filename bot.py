bot.py
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ከታች ባለው ' ' ውስጥ ያንተን የቦት ቶከን በትክክል ተካው
API_TOKEN = 'እዚህ ጋር የቦት ቶከንህን አስገባ' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "👋 እንኳን ደህና መጡ ወደ Birr Bot!\n\n"
        "እዚህ ማስታወቂያዎችን እና ቪዲዮዎችን በመመልከት በቀላሉ በቴሌብር ገንዘብ መስራት ይችላሉ።\n"
        "ለመጀመር ከታች ያለውን ሰማያዊ ቁልፍ ይጫኑ! 👇"
    )
    
    markup = InlineKeyboardMarkup()
    web_app_url = "https://televideoplayer.netlify.app"
    
    web_app_info = telebot.types.WebAppInfo(url=web_app_url)
    btn = InlineKeyboardButton(text="📺 ቪዲዮ እይና ብር ስራ", web_app=web_app_info)
    markup.add(btn)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

print("ቦቱ በትክክል መስራት ጀምሯል...")
bot.polling()
