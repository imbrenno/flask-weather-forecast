from flask import jsonify, Blueprint
from main.database.models.direct_geocoding_model import (
    DirectGeocoding,
    DirectGeocodingDTO,
)
from main.utils.log import log
import json
from main.services.api_direct_geo_sv import DirectGeocodingSv


bp = Blueprint(
    "direct_geo",
    __name__,
    template_folder="templates",
    url_prefix="/direct-geo",
)


class DirectGeocodingCtrl:

    @staticmethod
    @bp.route("/search-name/<city_name>", methods=["GET"])
    def get_geo_by_city_name(city_name):
        try:
            data = DirectGeocoding().get_one(str(city_name))
            if data:
                data_json = DirectGeocodingDTO(**data).to_json()
                return jsonify(json.loads(data_json)), 200

            data_get_geo = DirectGeocodingSv().get_geo(city_name)
            if data_get_geo:
                for item in data_get_geo:
                    direct_geo = DirectGeocodingDTO(
                        name=item["name"],
                        local_names=item["local_names"],
                        lat=item["lat"],
                        lon=item["lon"],
                        country=item["country"],
                        state=item["state"],
                    )

                    log.info(f"New geo data: {direct_geo}")
                    DirectGeocoding().save(direct_geo)

                return (
                    jsonify({"message": "busca com sucesso", "data": direct_geo}),
                    200,
                )

        except Exception as e:
            log.error(
                f"Error in DirectGeocodingCtrl 'get_geo_by_city_name' Exception: {e}"
            )
            return (
                jsonify(
                    {"message": "Erro ao consultar dados geograficos", "error": str(e)}
                ),
                500,
            )
