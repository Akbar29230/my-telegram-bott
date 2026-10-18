import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from google import genai

# Твои токены
TELEGRAM_TOKEN = "8844953749:AAG7YXaiZyWCnfsTXlQpTCFpwwShr46QeSE"
GEMINI_API_KEY = "AQ.Ab8RN6IqZOWUzs9MvGadf9ZsBUMr4XDzjzP_z8N2IRozOLPkMg"

# Инициализация бота и Gemini
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот с бесплатным искусственным интеллектом Gemini! Задай мне вопрос.")

# Обработка сообщений
@dp.message()
async def handle_ai_message(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:
        # Запрос к нейросети Gemini Flash
        response = ai_client.models.generate_content(
            model='gemini-3.8-flash',
            contents=message.text,
        )
        await message.answer(response.text)

    except Exception as e:
        await message.answer("Произошла ошибка при обращении к ИИ.")
        print(f"Ошибка в консоли: {e}")

# Запуск бота
async def main():
    print("Бот на Gemini успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())