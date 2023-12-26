from typing import Optional
from pydantic import BaseSettings,  SettingsConfigDict

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    
    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""
    model_config = SettingsConfigDict(env_file=".env")


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False

class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_")

class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="PROD_")

class TestConfig(GlobalConfig):
    DATABASE_URL = "sqlite:///data.db"
    DB_FORCE_ROLL_BACK: True

    model_config = SettingsConfigDict(env_prefix="TEST_")