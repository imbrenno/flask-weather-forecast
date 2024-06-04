from main.database.database import get_db
from dataclasses import dataclass, asdict
import json
from typing import Optional, Dict
from main.utils.log import log


@dataclass
class WeatherForecastDTO:
    city: Optional[Dict[str, str]]
    cnt: int
    cod: str
    list: Optional[Dict[str, str]]

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)


class WeatherForecast:
    def __init__(self):
        self.db = get_db()

    def save(self, data_forecast: WeatherForecastDTO):
        try:
            if not isinstance(data_forecast, WeatherForecastDTO):
                raise TypeError("data must be an instance of WeatherForecastDTO")
            result = self.db.weather_forecast.insert_one(asdict(data_forecast))
            log.info(f"Save new data in 'WeatherForecast': {result.inserted_id}")

        except Exception as e:
            log.error(f"Error in model WeatherForecast 'save' Exception: {e}")

    def get_all(self):
        return list(self.db.weather_forecast.find())

    def get_one(self, city: str):
        try:
            document = self.db.weather_forecast.find_one({"name": city})
            if document:
                document.pop("_id")
                log.info(f"get_one data in 'WeatherForecast': {document}")
                return document

            log.warning(f"No document found with name: {city}")
            return None
        except Exception as e:
            log.error(f"Error in WeatherForecast.get_one: {e}")
            return None

    def delete(self, city: str):
        query_filter = {"city": city}
        result = self.db.weather_forecast.delete_one(query_filter)
        log.info(
            f"Delete in weather_forecast, total of deleted: {result.deleted_count}"
        )

    def update(self, city: str, data: WeatherForecastDTO):
        query_filter = {"city": city}
        result = self.db.weather_forecast.update_one(
            query_filter, {"$set": data.__dict__}
        )
        log.info(
            f"Update in weather_forecast, total of updated: {result.modified_count}"
        )
