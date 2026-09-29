from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    api_base_url: str = "http://localhost:5000/api"

    class Config:
        env_file = ".env"


settings = Settings()
