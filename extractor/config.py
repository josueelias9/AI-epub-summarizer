"""
Configuration settings for the EPUB Extractor API
"""
import os
from typing import Optional

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
    API_PORT: int = int(os.getenv("API_PORT"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # EPUB processing settings
    EPUB_FILE: Optional[str] = os.getenv("EPUB_FILE")
    INPUT_PATH: str = os.getenv("INPUT_PATH")
    OUTPUT_PATH: str = os.getenv("OUTPUT_PATH")
    
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
  Input Path: {self.INPUT_PATH}
  Output Path: {self.OUTPUT_PATH}
"""

# Global settings instance
settings = Settings()