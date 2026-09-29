# EduFlow

Стек: Vue 3 (frontend) · C# / ASP.NET Core (backend) · PostgreSQL · Telegram-бот на Python (aiogram), общается с бэком по HTTP.

## Структура репозитория

```
EduFlow/
├── backend/                        # .NET solution (Clean Architecture)
│   ├── EduFlow.sln
│   ├── src/
│   │   ├── EduFlow.Api/            # ASP.NET Core Web API (контроллеры, DI, Program.cs)
│   │   ├── EduFlow.Application/    # интерфейсы, DTO, бизнес-логика
│   │   ├── EduFlow.Domain/         # сущности, enum'ы, без зависимостей
│   │   └── EduFlow.Infrastructure/ # EF Core, Npgsql, репозитории, миграции
│   └── tests/
│       └── EduFlow.UnitTests/
├── telegram-bot/                   # отдельный сервис, Python (aiogram)
│   ├── main.py
│   ├── app/
│   │   ├── config.py                # BOT_TOKEN, API_BASE_URL
│   │   ├── api_client.py             # httpx-клиент к EduFlow.Api
│   │   ├── dispatcher.py
│   │   └── handlers/
│   └── requirements.txt
├── frontend/                       # Vue 3 + Vite
│   ├── src/
│   │   ├── api/                    # axios-клиент
│   │   ├── components/
│   │   ├── router/
│   │   ├── stores/                 # pinia
│   │   └── views/
│   └── public/
├── .github/workflows/ci.yml        # build+test на пуш/PR
├── docker-compose.yml               # postgres + api + telegram-bot + frontend
├── .env.example
└── docs/
```

## Как сервисы связаны

```
Vue frontend  →  EduFlow.Api (C#)  →  PostgreSQL
                       ↑
              telegram-bot (Python)
```

Бот не трогает базу и не содержит бизнес-логики — только вызывает REST-эндпоинты `EduFlow.Api` через `httpx`. Внутри бэка: `Domain` ничего не знает про остальных, `Application` знает только про `Domain`, `Infrastructure` и `Api` знают про `Application`.

## Быстрый старт (локально, без Docker)

**Backend**
```bash
cd backend
dotnet restore
dotnet run --project src/EduFlow.Api
```

**Telegram-бот (Python)**
```bash
cd telegram-bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # вписать BOT_TOKEN, при необходимости API_BASE_URL
python main.py
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Через Docker Compose

```bash
cp .env.example .env    # вписать TELEGRAM_BOT_TOKEN
docker compose up --build
```

- API: http://localhost:5000/swagger
- Frontend: http://localhost:5173
- Postgres: localhost:5432 (eduflow / changeme)

## Что нужно доделать перед первым `git push`

1. `cd backend && dotnet new sln -n EduFlow` заново, затем `dotnet sln add src/**/*.csproj tests/**/*.csproj` — заглушка `.sln` в репо не содержит реальных GUID проектов.
2. `dotnet ef migrations add Initial --project src/EduFlow.Infrastructure --startup-project src/EduFlow.Api` — накатить первую миграцию под `User`.
3. Добавить `Dockerfile` в `EduFlow.Api/` (у `telegram-bot/` он уже есть).
4. На стороне API сделать реальный эндпоинт `POST /api/users/link-telegram`, который дёргает бот из `api_client.py` (сейчас это просто пример вызова).
5. Поменять `changeme` пароли перед деплоем.
