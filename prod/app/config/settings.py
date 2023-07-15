from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool = True
    rabbitmq_host: str
    rabbitmq_user: str
    rabbitmq_password: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()