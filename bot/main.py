from aiogram import Bot, Dispatcher, executor
from core.config import BOT_TOKEN
from handlers import messages

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

messages.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp)
