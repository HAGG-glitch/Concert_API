from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    # App info
    APP_NAME: str = "Theater Booking API"
    DEBUG: bool = False



# JWT settings
    SECRET_KEY: str = "AYS_123_321"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()