from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="6265333470:AAGKT_gFeVxmqXtMQ_fDR2Dfj9xQ9TCMzHM")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

def text_translator(text='text',src='en',dest='ru'):
    try:
        translator= Translator()
        translation = translator.translate(text=text,src=src,dest=dest)

        return translation.text
    except Exception as ex:
        return ex

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = (weather.current.temperature - 32) / 1.8

    region = weather.nearest_area.name + ". " + weather.nearest_area.region
    resp_msg = "В " + text_translator(text=region, src='en', dest='ru') + "\n"
    resp_msg += "Температура: " + str(round(celsius)) + "°.\n"
    resp_msg += text_translator(text=weather.current.description, src='en', dest='ru')

    if(celsius<=10):
        resp_msg += "\n\n Прохладно! Одевайся теплее!"
    else:
        resp_msg += "\n\n Тепло! Одевайся легче!"


    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)