from aiogram import types

async def set_defualt_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start bot"),
        types.BotCommand("help", "Help"),
        types.BotCommand("favorites", "You favorite coin"),
        types.BotCommand("about", "Read about coins"),
    ])