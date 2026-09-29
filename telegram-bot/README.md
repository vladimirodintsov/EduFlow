# EduFlow Telegram Bot (Python)

Отдельный сервис на aiogram 3. Общается с `EduFlow.Api` (C#) только по HTTP — своей базы и бизнес-логики не хранит.

## Структура

```
telegram-bot/
├── main.py                 # точка входа, poll-цикл
├── app/
│   ├── config.py           # BOT_TOKEN, API_BASE_URL из .env
│   ├── api_client.py       # httpx-клиент к EduFlow.Api
│   ├── dispatcher.py       # сборка роутеров aiogram
│   └── handlers/
│       ├── start.py        # /start
│       └── common.py       # фолбэк на нераспознанные сообщения
├── requirements.txt
├── Dockerfile
└── .env.example
```

## Запуск локально

```bash
cd telegram-bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # вписать BOT_TOKEN
python main.py
```

Бэк (`EduFlow.Api`) должен быть поднят на `API_BASE_URL` (по умолчанию `http://localhost:5000/api`).
