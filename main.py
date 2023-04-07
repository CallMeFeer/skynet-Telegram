import os
import openai
import telebot 
from dotenv import dotenv_values

config = dotenv_values(".env")

bot = telebot.TeleBot(config['TELEGRAM_TOKEN']) 
openai.api_key = config['OPENAI_TOKEN']

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Bienvenido, {name}! \nEscribe/Pregunta lo que desees. \n\nEste es un proyecto creado con el proposito de traer la tecnologia de ChatGPT a Telegram traido a ti por CallMeFeer.'.format(name=message.from_user.first_name))


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    user = str(message.text.split(' '))
    print(user)
    answer = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "user", "content": user }
		]
	)

    bot.send_message(message.chat.id, answer.choices[0].message.content)


bot.infinity_polling()