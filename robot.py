import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from main import router


# Функция конфигурирования и запуска бота
async def main():

    # Инициализируем бот и диспетчер
    bot = Bot(token='6129474314:AAEeqmPoSKVchVFjwn_sON0fPz6jtuwP4DM')
    dp = Dispatcher()
    storage = MemoryStorage()

    # Регистриуем роутеры в диспетчере
    dp.include_router(router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())