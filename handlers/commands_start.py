from aiogram import types
from misc import dp, bot
from .sqlit import reg_user, get_username
from .callbak_data import reg_p
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001612446247
reg_user(1,'SprintArbitraj')  # Запуск в БД
