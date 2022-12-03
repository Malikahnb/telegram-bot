import telebot
from telebot import types

bot = telebot.TeleBot('5626502754:AAG4vkxqLA4WBe8LUEpxSTQ79UZq4G9N-AE')

first = ''
second = ''
result = 0


@bot.message_handler(commands=['start'])
def start(message):
    name = f'Hello, <i>{message.from_user.first_name}</i> I am calculator bot! \n' \
           f'Send me /add, /subtract, /multiply or /divide'
    bot.send_message(message.chat.id, name, parse_mode='html')


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "add":
#         add(first_num())
#     elif call.data == "subtract":
#         bot.send_message(call.message.chat.id, 'Failed')


def first_num(message):  # asking for the input
    global first
    first = message.text
    bot.send_message(message.from_user.id, f'Please send the <b>first</b> number: ', parse_mode='html')
    # while first == 0:
    #     try:
    #         first = int(message.text)
    #     except Exception:
    #         bot.send_message(message.from_user.id, f'<b>Please send correct number!</b>', parse_mode='html')
    bot.register_next_step_handler(message, second_num)


def second_num(message):  # asking for the input
    global second
    second = message.text
    bot.send_message(message.from_user.id, f'Please send the <b>second</b> number: ', parse_mode='html')
    # while second == 0:
    #     try:
    #         second = int(message.text)
    #     except Exception:
    #         bot.send_message(message.from_user.id, f'<b>Please send correct number!</b>', parse_mode='html')
    bot.register_next_step_handler(message, operations)


@bot.message_handler(commands=['add'])
def add(message):
    first_num(message)
    global result
    if message == '/add':
        result = int(first) + int(second)
        bot.send_message(message.from_user.id, f'<i>Answer: </i>{result}', parse_mode='html')


@bot.message_handler(commands=['subtract'])
def add(message):
    first_num(message)
    global result
    if message == '/subtract':
        result = int(first) - int(second)
        bot.send_message(message.from_user.id, f'<i>Answer: </i>{result}', parse_mode='html')


@bot.message_handler(commands=['multiply'])
def add(message):
    first_num(message)
    global result
    if message == '/multiply':
        result = int(first) * int(second)
        bot.send_message(message.from_user.id, f'<i>Answer: </i>{result}', parse_mode='html')


@bot.message_handler(commands=['divide'])
def add(message):
    first_num(message)
    global result
    if message == '/divide':
        result = int(first) // int(second)
        bot.send_message(message.from_user.id, f'<i>Answer: </i>{result}', parse_mode='html')


@bot.message_handler(commands=['add', 'subtract', 'multiply', 'divide'])
def operations(message):
    while first == '':
        if message.text == '/add':
            bot.send_message(message.from_user.id, f'<i>Answer:</i>{first} + {second}', parse_mode='html')
        elif message.text == '/subtract':
            bot.send_message(message.from_user.id, f'<i>Answer:</i>{first} - {second}', parse_mode='html')
        elif message.text == '/multiply':
            bot.send_message(message.from_user.id, f'<i>Answer:</i>{first} * {second}', parse_mode='html')
        elif message.text == '/divide':
            bot.send_message(message.from_user.id, f'<i>Answer:</i>{first} // {second}', parse_mode='html')
        else:
            bot.send_message(message.from_user.id, 'Please enter the correct operation', parse_mode='html')
            break
        first_num(message)


bot.polling(none_stop=True)

# link to the source: https://habr.com/ru/post/442800/
