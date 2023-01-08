import telebot
import random

token = '5876915604:AAHhU-c5h21MiAkNPVWMQSqP1nb-IS3v-4U'

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи
запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавляет случайную задачу на дату Сегодня.
"""

RANDOM_TASKS = [
    "Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку",
    "Помыть машину"
]

tasks = {}


def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаем запись с ключом date
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = f'Задача {task} добавлена на дату {date}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'cегодня'
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = f'Задача {task} добавлена на дату {date}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text += '[]' + task + '\n'
    else:
        text = 'Задач на эту дату нет'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def helps(message):
    bot.send_message(message.chat.id, HELP)


bot.polling(none_stop=True)
