"""
This is a echo bot.
It echoes any incoming text messages.
"""



import logging
from checkword import checkWord


from aiogram import Bot, Dispatcher,executor, types


API_TOKEN = '6449412433:AAGzTzHZrQWi0Tkg7iFSFSxAlY72_aXB2Xo'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Uz imlo botiga hush kelibsiz")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Botdan foydalanish uchun so'z yuboring")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✔️{word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}"
        for text in result["matches"]:
            response+=f"✔️{text.capitalize()}\n"

    await message.reply(response)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
