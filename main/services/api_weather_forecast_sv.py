import requests
from typing import Dict
from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum
from main.utils.log import log


class WeahtherForecastSv:
    def __init__(self) -> None:
        self.api_url = Settings.get(
            hash=DotEnvEnum.WEATHER_FORECAST_API_URL.value,
        )
        self.api_key = Settings.get(
            hash=DotEnvEnum.WEATHER_FORECAST_API_KEY.value,
        )

    def get_forecast(self, data: Dict) -> None:
        try:
            url = f"{self.api_url}lat={data['lat']}&lon={data['lon']}&appid={self.api_key}"
            response = requests.get(url)
            if response:
                log.info(f"Response data WeahtherForecastSv 'get_forecast': {response.json()}")
                return response.json()

            return None
        except Exception as e:
            log.error(f"Error in WeahtherForecastSv 'get_forecast' Exception: {e}")
            return None
