import logging
import requests
from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum
from main.utils.log import log


class DirectGeocodingSv:
    def __init__(self) -> None:
        self.api_url = Settings.get(
            hash=DotEnvEnum.DIRECT_GEOCODING_API_URL.value,
        )
        self.api_key = Settings.get(
            hash=DotEnvEnum.WEATHER_FORECAST_API_KEY.value,
        )


    def get_geo(self, city_name: str) -> None:
        try:
            url = f"{self.api_url}q={city_name}&limit=1&appid={self.api_key}"
            response = requests.get(url)
            if response:
                log.info(f"Response data DirectGeocoding: {response.json()}")
                return response.json()

            return None
        except Exception as e:
            log.error(f"Error in DirectGeocoding 'excute' Exception: {e}")
            return None
