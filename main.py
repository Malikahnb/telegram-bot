# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5626502754:AAG4vkxqLA4WBe8LUEpxSTQ79UZq4G9N-AE')
#
# result = ''


# @bot.message_handler(commands=['start'])
# def start(message):
#     name = f'Hello, <i>{message.from_user.first_name}</i> I am calculator bot! \n' \
#            f'Send me /add, /subtract, /multiply or /divide'
#     bot.send_message(message.chat.id, name, parse_mode='html')
#
# @bot.message_handler(commands=['add'])
# def add(message):
#     return result =
#     bot.register_next_step_handler(result, first)
#     bot.send_message(message.chat.id, result)

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text.isdigit():
#         bot.send_message(message.chat.id, message, parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f'Your <b>ID</b>: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('world.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand u", parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Cool photo')


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     web = types.KeyboardButton('Visit us')
#     start = types.KeyboardButton('Hello')
#     markup.add(web, start)
#     bot.send_message(message.chat.id, 'Subscribe', reply_markup=markup)

# @bot.message_handler(commands=['add'])
# def add(message):
#     first(message)
#     second(message)
#     result = first + second
#     bot.send_message(message.chat.id, result)


# @bot.message_handler(content_types=['text'])
# def first(message):
#     first = bot.send_message(message.chat.id, f'Please send the <b>first</b> number: ', parse_mode='html')
#
#     if message.text in range(1, 100):
#         bot.register_next_step_handler(first, second)
    # else:
    #     bot.send_message(message.chat.id, f'<b>Please send the correct number: </b>', parse_mode='html')

    # if message.text != " ":
    #     bot.send_message(message.chat.id, second, parse_mode='html')

    # if first.isnumeric():
    #     second(message)
    # else:
    #     bot.send_message(message.chat.id, f'<b>Please send correct number!</b>', parse_mode='html')


# def second(message):
#     second = bot.send_message(message.chat.id, f'Please send the <b>second</b> number: ', parse_mode='html')
#

# def second(message):
#     second = f'Please send <b>second</b> number: '
#     bot.send_message(message.chat.id, second, parse_mode='html')
#
#     if second.isdigit() is True:
#         pass
#     else:
#         bot.send_message(message.chat.id, f'<b>Please send correct number!</b>', parse_mode='html')


# bot.polling(none_stop=True)
