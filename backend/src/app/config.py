from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    root_path: str = "http://127.0.0.1:8000"

    frontend_url: str = "http://127.0.0.1:5173"

    database_url: str = "sqlite:///./notes.db"

    model_config = SettingsConfigDict(env_file='.env')

    qr_code_url: str = "{frontend_url}/qr?token={token}"

settings = Settings()
""""""