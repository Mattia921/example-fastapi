from pydantic import BaseSettings

"""
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
"""

class Settings(BaseSettings):
    database_hostname = "localhost"
    database_port = "5432"
    database_password = "Mattia92"
    database_name = "fastapi"
    database_username = "postgres"
    secret_key = "f646ce0b45db3e9dec6ab24a47c7a480f56624e5065edced4e921ab815cfa77b"
    algorithm = "HS256"
    access_token_expire_minutes = 60



settings = Settings()
