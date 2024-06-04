from flask import jsonify, Blueprint, request
from main.database.models.weather_forecast_model import (
    WeatherForecast,
    WeatherForecastDTO,
)
from main.services.api_weather_forecast_sv import WeahtherForecastSv
from main.utils.log import log

bp = Blueprint(
    "weather_forecast",
    __name__,
    template_folder="templates",
    url_prefix="/weather-forecast",
)


class WeatherForecastCtrl:

    @staticmethod
    @bp.route("/five-days-details", methods=["GET"])
    def get_five_day_forecast_details():
        try:
            data = request.get_json()
            get_forecast = WeahtherForecastSv().get_forecast(data)
            log.info(f"DATA, get_forecast: {get_forecast}")
            if get_forecast:
                forecast = WeatherForecastDTO(
                    city=get_forecast["city"],
                    cnt=get_forecast["cnt"],
                    cod=get_forecast["cod"],
                    list=get_forecast["list"],
                )
                WeatherForecast().save(forecast)
            return jsonify(get_forecast)

        except Exception as e:
            log.error(
                f"Error in WeatherForecastCtrl 'get_five_day_forecast_details' Exception: {e}"
            )
            return jsonify({"message": "Erro ao buscar precisao", "error": str(e)}), 500
