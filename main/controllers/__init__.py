from main.controllers.direct_geocoding_ctrl import bp as direct_geocoding_bp
from main.controllers.weather_forecast_ctrl import bp as weather_forecast_bp

blueprints_ctrl = [
    direct_geocoding_bp,
    weather_forecast_bp,
]
