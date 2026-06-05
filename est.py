import asyncio
import aiohttp


async def test_connection():
    # Если используешь Вариант 2, раскомментируй строку ниже и укажи свой порт:
    # proxy = "http://127.0.0.1:10809"
    # async with aiohttp.ClientSession() as session:
    #     async with session.get('https://api.telegram.org', proxy=proxy) as resp:

    # Если используешь TUN-режим (Вариант 1):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.telegram.org') as resp:
            print("Статус ответа:", resp.status)
            if resp.status == 200:
                print("Ура! Соединение с Telegram установлено!")
            else:
                print("Что-то пошло не так...")


asyncio.run(test_connection())