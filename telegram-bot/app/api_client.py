"""Тонкий клиент для похода в C#-бэк (EduFlow.Api)."""
import httpx

from app.config import settings


class ApiClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(base_url=settings.api_base_url, timeout=10)

    async def ping(self) -> dict:
        resp = await self._client.get("/users/ping")
        resp.raise_for_status()
        return resp.json()

    async def link_telegram_account(self, chat_id: int, telegram_username: str | None) -> dict:
        """Пример: привязать telegram chat_id к пользователю в системе."""
        resp = await self._client.post(
            "/users/link-telegram",
            json={"chatId": chat_id, "telegramUsername": telegram_username},
        )
        resp.raise_for_status()
        return resp.json()

    async def close(self) -> None:
        await self._client.aclose()


api_client = ApiClient()
