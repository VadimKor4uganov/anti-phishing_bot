# Telegram Bot

Проект разрабатывался ~2 месяца.
Бот анализирует сообщения и ссылки на признаки фишинга.

## Требования
- Python 3.10 или выше
- venv (встроенный модуль Python)

## Стек технологий
| Компонент | Версия |
|-----------|--------|
| Python    | 3.10+  |
| aiogram   | 2.25.1 |
| aiohttp   | 3.8.6  |

## Виртуальное окружение

Проект использует встроенный модуль Python `venv` для изоляции зависимостей.

# ПОЛНАЯ ИНСТРУКЦИЯ

1. Клонирование репозитория:
```bash
git clone https://github.com/VadimKor4uganov/anti-phishing_bot.git
cd bot
```

2. Создание виртуального окружения:
```bash
python3.10 -m venv venv

# Активация (Linux/Mac)
source venv/bin/activate

# Активация (Windows)
venv\Scripts\activate
```

3. Установка зависимостей:
```bash
pip install aiogram==2.25.1
```

4. Конфигурация:
Добавьте токен вашего бота в файл bot/core/config.py:
```python
BOT_TOKEN = "ваш_токен_от_botfather"
```

5. Запуск:
```bash
python main.py
```

6. Настройка списков:
- bot/data/whitelist_sites.txt
- bot/data/suspicious_words.txt
