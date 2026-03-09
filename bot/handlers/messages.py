from aiogram import types
from utils.analyzer import analyze_message
import re

def register(dp):
    @dp.message_handler(commands=['start'])
    async def start_cmd(message: types.Message):
        if message.chat.type == 'private':
            await message.reply(
                "👋 Привет! Я бот для защиты групп от фишинга.\n\n"
                "📌 **Как добавить в группу:**\n"
                "1. Добавьте меня в группу\n"
                "2. Сделайте меня **администратором**\n"
                "3. Выдайте **права на удаление сообщений**\n\n"
                "⚙️ **Необходимые права администратора:**\n"
                "✅ Удаление сообщений\n"
                "✅ (опционально) Блокировка пользователей\n\n"
                "🔍 **Что я делаю:**\n"
                "• Проверяю сообщения на подозрительные слова\n"
                "• Обнаруживаю фишинговые ссылки\n"
                "• Удаляю опасные сообщения\n"
                "• Предупреждаю группу об угрозе"
            )
        else:
            bot_member = await message.bot.get_chat_member(message.chat.id, message.bot.id)
            
            if bot_member.can_delete_messages:
                await message.reply("✅ Бот работает! Есть права на удаление сообщений.")
            else:
                await message.reply(
                    "⚠️ **Внимание!**\n"
                    "У бота нет прав на удаление сообщений.\n\n"
                    "Сделайте меня администратором и включите:\n"
                    "• Удаление сообщений"
                )
    
    @dp.message_handler()
    async def check(message: types.Message):
        if not message.text:
            return
            
        result = analyze_message(message.text)
        if result:
            try:
                await message.delete()
            except Exception as e:
                print(f"Не удалось удалить сообщение: {e}")
            
            safe_text = make_links_safe(message.text[:200])
            
            warning_text = f"⚠️ Обнаружен и удален фишинг: {result}\n"
            warning_text += f"Пользователь: @{message.from_user.username or 'нет username'}\n"
            warning_text += f"Сообщение содержало:\n{safe_text}"
            
            await message.answer(warning_text)

def make_links_safe(text):
    if not text:
        return text
    
    url_pattern = r'(https?://[^\s]+)'
    
    def replace_url(match):
        url = match.group(1)
        return f'`{url}`'
    
    domain_pattern = r'(?<![@/\w])([a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]?\.[a-zA-Z]{2,})(?![^\s])'
    
    text = re.sub(url_pattern, replace_url, text)
    text = re.sub(domain_pattern, r'`\1`', text)
    
    return text
