import telebot
from telebot import types

bot = telebot.TeleBot('5626502754:AAG4vkxqLA4WBe8LUEpxSTQ79UZq4G9N-AE')

first = 0
second = 0
result = 0


@bot.message_handler(commands=['start'])
def start(message):
    name = f'Hello, <i>{message.from_user.first_name}</i> I am calculator bot! \n' \
           f'Send me /add, /subtract, /multiply or /divide'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=['add', 'subtract', 'multiply', 'divide'])
def operations(message):
    while first == 0:
        if message.text == '/add':
            bot.send_message(message.from_user.id, f'{first} + {second}')
        elif message.text == '/subtract':
            bot.send_message(message.from_user.id, f'{first} - {second}')
        elif message.text == '/multiply':
            bot.send_message(message.from_user.id, f'{first} * {second}')
        elif message.text == '/divide':
            bot.send_message(message.from_user.id, f'{first} // {second}')
        else:
            bot.send_message(message.from_user.id, 'Please enter the correct operation')
    first_num(message)

# @bot.message_handler(content_types=['text'])
# def operations(message):
#     if message.text == "/add":
#         first_num(message)
#         return int(result) == first + second
#     elif message.text == "/subtract":
#         return int(result) == int(first) - int(second)
#     elif message.text == "/multiply":
#         return int(result) == int(first) * int(second)
#     elif message.text == "/divide":
#         return int(result) == int(first) / int(second)
#
#     bot.send_message(message.chat.id, result)


def first_num(message):
    global first
    first = message.text
    bot.send_message(message.from_user.id, f'Pleas e send the <b>first</b> number: ', parse_mode='html')
    while first == 0:
        try:
            first = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, f'<b>Please send correct number!</b>', parse_mode='html')
    bot.register_next_step_handler(message, second_num)


def second_num(message):
    global second
    second = message.text
    bot.send_message(message.from_user.id, f'Please send the <b>second</b> number: ', parse_mode='html')
    while second == 0:
        try:
            second = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, f'<b>Please send correct number!</b>', parse_mode='html')
    bot.register_next_step_handler(message, operations)


bot.polling(none_stop=True)

# create separate def to perform operations, and link them to the first start function
# link to the source: https://habr.com/ru/post/442800/
