import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('8180337380:AAGTisNcXU6MQk5shLZDif11Ubx-S4smvks')

reminder_threads = {}
list = ["Мёд не портится: Археологи, исследуя древние египетские гробницы, обнаружили горшочки с мёдом, которому более 3000 лет. Этот мёд оказался всё ещё съедобным! Это связано с его уникальными свойствами, такими как низкое содержание воды и высокая кислотность, которые предотвращают рост бактерий.",
        "Шоколад как валюта: В древней Мезоамерике, особенно среди цивилизаций майя и ацтеков, какао-бобы использовались как форма валюты. Эти бобы были настолько ценными, что их обменивали на товары и услуги. Например, за 100 какао-бобов можно было купить раба.",
        "Томат — фрукт: В ботаническом смысле, томат считается фруктом, потому что он развивается из цветка и содержит семена. Однако в кулинарии его обычно относят к овощам из-за его менее сладкого вкуса и использования в салатах и других несладких блюдах. В 1893 году Верховный суд США даже принял решение считать томат овощем в рамках тарифного законодательства."]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я бот, который будет тебе напоминать вовремя поесть!')
    reminder_thread = threading.Thread(target = send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о еде: {random_fact}')

def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "12:00"
    end_rem = "03:10"
    while True:
        now = datetime.datetime.now()
        now = datetime.datetime.now().strftime("%H:%M")
        if now == second_rem or now == first_rem or now == end_rem:
            bot.send_message(chat_id, "Пора перекусить")
            time.sleep(61)
            time.sleep(1)

@bot.message_handler(commands=["help"])
def help_message(message):
    help_text = (
        "Доступные команды:\n" 
        "/start - Запустить бота и начать получать напоминания.\n" 
        "/fact - получить интересный факт о еде.\n" 
        "/help - Показать это сообщение.\n"
        "/support - Служба поддержки.\n"
        "/about - Информация о боте.\n"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=["support"])
def support_message(message):
    support_text = (
        "Если у вас возникли вопросы или нужна поддержка, пожалуйста, свяжитесь с нами:\n\n"
        "Электронная почта: support@example.com\n"
        "Телефон: +1234567890\n"
        "Вы также можете оставить сообщение в этом чате, и мы постараемся ответить как можно скорее."
    )
    bot.reply_to(message,support_text)

@bot.message_handler(commands=["about"])
def about_message(message):
    about_text = (
        "Привет! Я бот напоминаний о еде, созданный для того, чтобы помогать вам вовремя перекусывать и узнавать интересные факты о еде.\n\n"
        "Моя основная задача - отправлять напоминания в определенное время, чтобы вы не забывали перекусить.\n"
        "Также я могу рассказать интересные факты о еде, которые могут вас удивить!\n\n"
        "Если у вас есть предложения или вы нашли ошибку, пожалуйста, свяжитесь с нами по электронной почте: support@example.com "
    )
    bot.reply_to(message, about_text)



bot.polling(non_stop=True)