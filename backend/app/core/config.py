import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME = os.getenv(
        "APP_NAME",
        "SmartTrafficAI API",
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "0.1.0",
    )

    DEBUG = os.getenv(
        "DEBUG",
        "false",
    ).lower() == "true"

    MONGODB_URL = os.getenv(
        "MONGODB_URL",
        "",
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "smarttrafficai",
    )


settings = Settings()