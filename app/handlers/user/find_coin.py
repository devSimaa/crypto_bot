from aiogram import types, Dispatcher
from loader import dp, bot, _
from app.others.binance import searc_coin
from app.keyboards.inline_keyboard import add_favorite_ikb

@dp.message_handler()
async def find_coin(message: types.Message):
    user_msg = message.text.upper() + "USDT"
    try:
        text = searc_coin(user_msg)
        await message.answer(
            text=text,
            reply_markup=await add_favorite_ikb(user_msg)
        )
    except:
        error_text = 'Coin nor found!\nTry again.'
        await message.answer(
            text=error_text,
        )
