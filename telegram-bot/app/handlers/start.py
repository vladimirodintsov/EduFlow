from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.api_client import api_client

router = Router(name="start")


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    try:
        status = await api_client.ping()
        backend_state = f"бэк отвечает: {status.get('status')}"
    except Exception:
        backend_state = "бэк недоступен, но бот жив"

    await message.answer(
        f"Привет! Это EduFlow-бот.\n{backend_state}"
    )
