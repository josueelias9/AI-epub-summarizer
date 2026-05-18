"""
Configuration settings for the summary worker
"""

import os


class Settings:
    """Application settings loaded from environment variables"""

    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_NAME: str = os.getenv("POSTGRES_DB")

    LLM_MODEL: str = os.getenv("LLM_MODEL")
    LLM_HOST: str = os.getenv("LLM_HOST")
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/%2F")
    SUMMARY_QUEUE_NAME: str = os.getenv("SUMMARY_QUEUE_NAME", "summary_jobs")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
