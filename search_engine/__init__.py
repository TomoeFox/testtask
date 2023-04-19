import abc

from typing import Dict

import requests

from config.search import search_conf


class SearchElementInterface(abc.ABC):

    ENTITY_TYPES: Dict[str, list]
    ATTRIBUTE_TYPES: Dict[str, list]
    MEDIA_TYPES: list

    def __init__(self, artist_name: str, value: str):
        self.artist_name = artist_name.lower()
        self.value = value.lower()
        self.search_entity_type = None
        self.search_media_type = None
        self.search_attribute_type = None

    def set_entity_type(self, value: str):
        if value not in self.ENTITY_TYPES.get(self.search_media_type, []):
            raise ValueError(f"Wrong entity type {value}")
        self.search_entity_type = value

    def set_media_type(self, value: str) -> None:
        if value not in self.MEDIA_TYPES:
            raise ValueError(f"Wrong media type {value}")
        self.search_media_type = value

    def set_attribute_type(self, value: str) -> None:
        if value not in self.ATTRIBUTE_TYPES.get(self.search_entity_type, []):
            raise ValueError(f"Wrong media type {value}")
        self.search_attribute_type = value

    @abc.abstractmethod
    def prepare_request(self) -> dict:
        ...


class SearchEngineInterface(abc.ABC):

    def __init__(self, param_name):
        self.base_url = getattr(search_conf, param_name, None)

    def execute(self, element: SearchElementInterface):
        result = requests.get(self.base_url, **element.prepare_request())
        return self.handle_result(result.text)

    @abc.abstractmethod
    def handle_result(self, result: str):
        ...
