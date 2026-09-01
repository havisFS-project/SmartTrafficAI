from os import getenv

from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME: str = getenv(
        "APP_NAME",
        "SmartTrafficAI API",
    )

    APP_VERSION: str = getenv(
        "APP_VERSION",
        "0.1.0",
    )

    DEBUG: bool = getenv(
        "DEBUG",
        "false",
    ).lower() == "true"


settings = Settings()