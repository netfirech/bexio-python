from pydantic import BaseSettings


class Settings(BaseSettings):
    bexio_api_key: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
