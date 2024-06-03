from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum

DEBUG = True
MONGO_URI = Settings.get(DotEnvEnum.MONGO_URI.value)
