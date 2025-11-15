import cloudinary
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    # ---------------- Database ----------------
    sqlalchemy_database_url: str
    postgres_db: str

    # ---------------- Auth ----------------
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 1440
    expire_minutes: int = 60  

    # ---------------- Email ----------------
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str

    # ---------------- Redis ----------------
    redis_url: str

    # ---------------- Cloudinary ----------------
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )


settings = Settings()


def init_cloudinary():
    """
    Initialize Cloudinary configuration using credentials from settings.
    """
    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET")
    )
