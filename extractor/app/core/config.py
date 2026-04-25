"""
Configuration settings for the EPUB Extractor API
"""
import os

class Settings:
    """Application settings loaded from environment variables"""
    
    # Database settings
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_NAME: str = os.getenv("POSTGRES_DB")
    
    # API settings
    API_HOST: str = os.getenv("API_HOST")
    API_PORT: int = os.getenv("API_PORT")
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    LLM_MODEL: str = os.getenv("LLM_MODEL")
    LLM_HOST: str = os.getenv("LLM_HOST")



    @property
    def database_url(self) -> str:
        """Get the complete database URL"""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    def __str__(self) -> str:
        """String representation of settings (excluding sensitive data)"""
        return f"""Settings:
  Database: {self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}
  API: {self.API_HOST}:{self.API_PORT}
  Debug: {self.DEBUG}
"""

# Global settings instance
settings = Settings()