import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status, get_username, reg_user

import random

text_stop = """Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала посмотри видео, а потом нажимай🙏🙃"""

text_dogon = """Я вижу ты ещё не посмотрел(а) видосик и не вник в суть😎

Зачем забивать? Го зарабатывать 💸"""

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001612446247


class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, 'SprintArbitraj')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🔥Погнали дальше 🔥', callback_data='sprint_online')
    markup.add(bat_a)

    q = await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=295)
    await asyncio.sleep(15)
    await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=q.message_id, reply_markup=markup)


@dp.callback_query_handler(lambda call: True, state='*')
async def answer_push_inline_button(call, state: FSMContext):
    if call.data == 'sprint_online':
        change_status(call.message.chat.id, num=11) #1 (Погнали дальше)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔥 Давай 🔥', callback_data='go_1')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=298)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=300)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=302)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=304)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=305,reply_markup=markup)

    if call.data == 'go_1':
        change_status(call.message.chat.id, num=22) #2 (Давай)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='А что за Идея?', callback_data='go_2')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=308, reply_markup=markup)

    if call.data == 'go_2':
        await state.update_data(video1='stop')
        change_status(call.message.chat.id, num=33) #3 (Что за идея)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Погнали 💪', callback_data='go_3')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=311)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=312, reply_markup=markup)
        await asyncio.sleep(60)  # 60 секунд
        await state.update_data(video1='start')

    if call.data == 'go_3':
        change_status(call.message.chat.id, num=44)  # 4 (Погнали, голосовой)
        try:
            if ((await state.get_data())['video1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='😎оп оп😎', callback_data='go_4')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=171)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=177,reply_markup=markup)





    if call.data == 'go_4':
        change_status(call.message.chat.id, num=55) #5 (нажали на видос 😎оп оп😎)
        await state.update_data(v2='false')
        try:
            if ((await state.get_data())['video1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(v1='true')
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🔎ТЕСТ🔍', callback_data='go_10')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=182,
                                   reply_markup=markup)

        await asyncio.sleep(1800)  # 30 минут
        try:
            if ((await state.get_data())['v2']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

        await asyncio.sleep(3600)  # 60 минут
        try:
            if ((await state.get_data())['v2']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

        await asyncio.sleep(86400)  # 24 часа
        try:
            if ((await state.get_data())['v2']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

    if call.data == 'go_10':
        await state.update_data(v2='true')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='1️⃣', callback_data='ans_t')
        bat_b = types.InlineKeyboardButton(text='2️⃣', callback_data='ans_f')
        bat_c = types.InlineKeyboardButton(text='3️⃣', callback_data='ans_f')
        markup.add(bat_a, bat_b, bat_c)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=184, reply_markup=markup)

    if call.data == 'ans_f':
        await bot.send_message(chat_id=call.message.chat.id, text='Нет, это не арбитраж. Попробуй ещё раз')

    if call.data == 'ans_t':
        change_status(call.message.chat.id, num=66) #Прошли тест

        await state.update_data(video2='stop')
        await state.update_data(v3='false')

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='НАЧАТЬ ДЕЙСТВОВАТЬ⚡️', callback_data='go_12')
        markup.add(bat_a)

        await bot.send_message(chat_id=call.message.chat.id, text='Красава😎 Двигаемся дальше')
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=187, reply_markup=markup)
        await asyncio.sleep(120)  # 120 секунд
        await state.update_data(video2='start')
        await asyncio.sleep(1800)  # 30 минут
        try:
            if ((await state.get_data())['v3']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

        await asyncio.sleep(3600)  # 60 минут
        try:
            if ((await state.get_data())['v3']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

        await asyncio.sleep(86400)  # 24 часа
        try:
            if ((await state.get_data())['v3']) == 'true':
                flag = True
            else:
                flag = False
        except:
            flag = True
        if flag == False:
            await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

    if call.data == 'go_12':
        change_status(call.message.chat.id, num=77)
        try:
            if ((await state.get_data())['video2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(v3='true')
            await state.update_data(v4='false')
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Готово✅️', callback_data='go_111')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=195)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=196,
                                   reply_markup=markup)
            await asyncio.sleep(1800)  # 30 минут
            try:
                if ((await state.get_data())['v4']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

            await asyncio.sleep(3600)  # 60 минут
            try:
                if ((await state.get_data())['v4']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

            await asyncio.sleep(86400)  # 24 часа
            try:
                if ((await state.get_data())['v4']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_dogon)

    if call.data == 'go_111':
        await state.update_data(v4='true')
        change_status(call.message.chat.id, num=1)
        try:
            user = get_username(call.message.chat.id)
        except:
            user = 'SprintBekir'

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=199, caption=f"""Обязательно смотри видео!

Моя инста👉 https://instagram.com/bekirsariev
подписывайся, будем дружить 

Мой телеграм 👉 @{user}""")

        await asyncio.sleep(180)  # 180

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=202)
        await asyncio.sleep(180)  # 180

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=250, caption=f"""🚀 Залетай, пока мы готовы учить и вкладываться в тебя по полной программе!

Осталось 9 мест

Гооо 💸 @{user}

P.s
Пожалуйста, пиши после просмотра
всех видео! Давай ценить 
время, друг друга!🙏🏻""")
        await asyncio.sleep(86400)  # 86 400

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=207, caption=f"""Мишаня, сделал почти 100$ за день, примерно 4 месяца назад, он попал в спринт, полным нулём)

И рассказывал, как устал зависеть от родаков!

Как ему стыдно просить деньги, и хочется самостоятельно, себя обеспечивать!

Не понимаю подростков, есть телефон, есть интернет, а они не пользуются этим 🤧

Задумайся☝️ мы ещё готовы помочь тебе, начать зарабатывать в интернете.

Вперёд 🤘@{user}""")
        await asyncio.sleep(21600)  # 21 600
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=210, caption=f"""Ааааа🙀 10.6 🍋🍋🍋

Просто глянь, видосик 😎

Тяжело передать насколько я в афиге от нашей движухи, но это просто разнос!

Не упускай, действуй, зарабатывай!

Вливайся 💪 @{user}""")

        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=213, caption=f"""30$ за вечер🔥

Согласись неплохо? Учитывая, что это без образования, и похода на некайфовую работу 🤮

Бабки = свобода
Делать то что ты хочешь, и брать от жизни максимум, особенно пока ты молод!

Куча ребят сидят 
без денег, и думают что 
все впереди 🤣

❗️Сейчас надо рубить капусту, сейчас получай максимальное удовольствие от жизни.

Гоооу с нами🚀 @{user}""")
        await asyncio.sleep(43200)  # 43 200

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=216, caption=f"""33 доллара за 2 часа, ну что за 
тигр 🐅

Телега сейчас на пике прибыльности, и простоты)

Это факт, который ясен не многим, зачем искать подработку, если есть Телеграм под носом!

Моё предложение, раскрутить свой канал без вложений, все ещё в силе!

Хватит быть массой, пошли в 
команду, зарабатывать 
по кайфу💰 

👉 @{user}""")

        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=219, caption=f"""67$ как с пола подобрать!

- Кто то батрачит, а кто то заливает ролики в тик ток 😎

- Кто то ноет как все плохо, а кто то уже начал действовать!

- Кто то читает этот текст, а кто то уже помогает семье, и растит свой канал!

А что выберешь ты? 

1) Газ в пол 🚘 @{user}
2) Упустить последний шанс!""")
        await asyncio.sleep(21600)  # 21 600
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=222)
        await bot.send_message(chat_id=call.message.chat.id, text=f"""Ты полностью посмотрел(а) этого бота, но до сих пор не вышел(а) на заработок? А ведь ты так хотел(а) поднять бабок… и бросил(а) на пол пути.

Жду в Спринте ! 
(будем учиться) 

Либо можешь продолжить бояться и остаться на месте…

Получить мечту🏎
👉 @{user}""")
        await asyncio.sleep(86400)  # 86 400
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=257, caption=f"""⛔️МЕСТА по скидке ЗАКОНЧИЛИСЬ⛔️

Но если ты готов 
Тогда можем лично для тебя
Оставить скидку👉 @{user}""")
        await asyncio.sleep(86400)  # 86 400
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=258)

    if call.data == 'bat_video2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='12-17', callback_data='sprint_online')
        bat_b = types.InlineKeyboardButton(text='18+', callback_data='bat_video3')
        markup.add(bat_a, bat_b)
        await bot.send_message(chat_id=call.message.chat.id, text='Сколько тебе лет?', reply_markup=markup)

    if call.data == 'bat_video3':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Да', callback_data='bat_video4')
        bat_b = types.InlineKeyboardButton(text='Нет', callback_data='sprint_online')
        markup.add(bat_a, bat_b)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты из Ташкента?', reply_markup=markup)

    if call.data == 'bat_video4':
        await bot.send_message(chat_id=call.message.chat.id, text="""Для жителей Ташкента, есть специальное предложение🔥
Подробности тут👉https://t.me/TashkentTelebot""")

    try:
        await bot.answer_callback_query(call.id)
    except:
        pass
