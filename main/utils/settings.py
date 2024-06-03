import os
from dotenv import load_dotenv


class Settings:
    @staticmethod
    def get(hash: str) -> str:
        load_dotenv()
        return os.getenv(hash.upper(), "")
