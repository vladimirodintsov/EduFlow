from aiogram import Dispatcher

from app.handlers import start, common


def build_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(common.router)  # общий фолбэк — регистрируем последним
    return dp
