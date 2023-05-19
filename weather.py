import python_weather
import asyncio
import os

async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:

        weather = await client.get("Каменск-уральский")
        celsius = (weather.current.temperature-32) / 1.8

        print(str(round(celsius))+"°")
        #print(weather.current.temperature)

        print(weather.current.description)
        print(weather.nearest_area.name)


        # for forecast in weather.forecasts:
        #     print(forecast.date, forecast.astronomy)
        #
        #     # hourly forecasts
        #     for hourly in forecast.hourly:
        #         print(f' --> {hourly!r}')


if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())



    #_______________________________
    from aiogram import Bot, Dispatcher, executor, types
    from googletrans import Translator
    import python_weather
    import asyncio
    import os

    # bot init
    bot = Bot(token="6265333470:AAGKT_gFeVxmqXtMQ_fDR2Dfj9xQ9TCMzHM")
    dp = Dispatcher(bot)
    client = python_weather.Client(format=python_weather.IMPERIAL)


    def text_translator(text='Hello friend', src='en', dest='ru'):
        try:
            translator = Translator()
            result = print(translator.translate(text='Hello friend', src='en', dest='ru'))
            return result.text
        except Exception as ex:
            return ex


    # echo
    @dp.message_handler()
    async def echo(message: types.Message):
        weather = await client.get(message.text)
        celsius = (weather.current.temperature - 32) / 1.8
        print(text_translator(text='hello', src='en', dest='ru'))  # состояние
        print(weather.nearest_area.name)  # Регион
        resp_msg = message.text
        await message.answer(str(round(celsius)) + "°")


    # run long-polling
    if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)














