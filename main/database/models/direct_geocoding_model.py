from main.database.database import get_db
from dataclasses import dataclass, asdict
import json
from typing import Optional, Dict
from main.utils.log import log


@dataclass
class DirectGeocodingDTO:
    name: str
    local_names: Optional[Dict[str, str]]
    lat: float
    lon: float
    country: str
    state: str

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)


class DirectGeocoding:
    def __init__(self):
        self.db = get_db()

    def save(self, data: DirectGeocodingDTO):
        try:
            if not isinstance(data, DirectGeocodingDTO):
                raise TypeError("data must be an instance of DirectGeocodingDTO")
            result = self.db.direct_geocoding.insert_one(asdict(data))
            log.info(f"Save new data in 'DirectGeocoding': {result.inserted_id}")
        except Exception as e:
            log.error(f"Error in model DirectGeocoding 'save' Exception: {e}")

    def get_all(self):
        try:
            documents = list(self.db.direct_geocoding.find())
            for doc in documents:
                doc.pop("_id", None)
            log.info(
                f"get_all data in 'DirectGeocoding': {len(documents)} documents found"
            )
            return documents
        except Exception as e:
            log.error(f"Error in DirectGeocoding.get_all: {e}")
            return []

    def get_one(self, name: str):
        try:
            document = self.db.direct_geocoding.find_one({"name": name})
            if document:
                document.pop("_id")
                log.info(f"get_one data in 'DirectGeocoding': {document}")
                return document

            log.warning(f"No document found with name: {name}")
            return None
        except Exception as e:
            log.error(f"Error in DirectGeocoding.get_one: {e}")
            return None

    def delete(self, name: str):
        try:
            query_filter = {"name": name}
            result = self.db.direct_geocoding.delete_one(query_filter)
            log.info(
                f"Delete in direct_geocoding, total of deleted: {result.deleted_count}"
            )
        except Exception as e:
            log.error(f"Error in DirectGeocoding.delete: {e}")

    def update(self, name: str, data: DirectGeocodingDTO):
        try:
            if not isinstance(data, DirectGeocodingDTO):
                raise TypeError("data must be an instance of DirectGeocodingDTO")
            query_filter = {"name": name}
            result = self.db.direct_geocoding.update_one(
                query_filter, {"$set": asdict(data)}
            )
            log.info(
                f"Update in direct_geocoding, total of updated: {result.modified_count}"
            )
        except Exception as e:
            log.error(f"Error in DirectGeocoding.update: {e}")
