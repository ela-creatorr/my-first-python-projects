# =======================================================
# РАЗРАБОТЧИК: Еламан Оспан
# СПЕЦИАЛИЗАЦИЯ: Python Backend & Automation Developer
# ТЕЛЕГРАМ: https://t.me/coderela
# ПРОФИЛЬ FL.RU: https://www.fl.ru/users/elamanospan20/portfolio/
# ГИТХАБ: https://github.com/ela-creatorr
# =======================================================

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8639074470:AAHLg_VtW9DRyWwPLhdynARRWR88cLJvop4"
ADMIN_ID = 8296533246

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💼 Мои Услуги"), KeyboardButton(text="📊 Прайс-лист")],
        [KeyboardButton(text="📞 Заказать разработку")]
    ],
    resize_keyboard=True
)

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! 👋\n"
        "Я бот-визитка Python-разработчика. Чем могу помочь?",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "💼 Мои Услуги")
async def show_services(message: Message):
    await message.answer(
        "🔥 Мои ключевые навыки:\n"
        "• Разработка Telegram-ботов любой сложности\n"
        "• Парсинг данных и выгрузка в Excel\n"
        "• Автоматизация рутинных задач"
    )

@dp.message(F.text == "📊 Прайс-лист")
async def show_price(message: Message):
    await message.answer(
        "💰 Ориентировочная стоимость работ:\n"
        "• Простой бот / Скрипт: от 3 000 руб.\n"
        "• Сложный бот с базой данных: от 8 000 руб.\n"
        "• Парсер сайтов: от 4 000 руб."
    )

@dp.message(F.text == "📞 Заказать разработку")
async def order_service(message: Message):
    await message.answer("Отличный выбор! Напишите мне в личные сообщения: @coderela")
    
    try:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 Сигнал! Пользователь @{message.from_user.username} (ID: {message.from_user.id}) нажал кнопку 'Заказать разработку'!"
        )
    except Exception:
        pass

async def main():
    print("Бот успешно запущен и работает...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
