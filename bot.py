import telebot
import openai
from decouple import config

# устанавливаем ключ API OpenAI из переменной окружения
openai.api_key = config('OPENAI_API_KEY')

# создаем экземпляр телеграм бота
token = config('TOKEN')
bot = telebot.TeleBot(token)


# создаем обработчик команд
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 "Привет! Я бот, который может отвечать на ваши вопросы с помощью с OpenAI.\n Просто задай вопрос и жди ответа.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
                 "Вы можете отправлять запросы в OpenAI через меня. Просто напишите мне свой запрос и я отправлю его на обработку.")


# создаем обработчик сообщений
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Запрос принят в работу.")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=3500
        )
        bot.reply_to(message, response.choices[0].text)
    except:
        bot.reply_to(message, "Произошла ошибка при обработке вашего запроса.")


# запускаем телеграм бота
bot.polling()
