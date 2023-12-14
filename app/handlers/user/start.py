from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot, _
from database.connect import newUsr

@dp.message_handler(CommandStart())
async def comm_start(message: types.Message):
    text = _(f"👋, <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>")
    await message.answer(text)
    newUsr(message.from_user.id)
