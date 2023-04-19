import abc

from typing import Dict

import requests

from config.search import search_conf


class SearchElementInterface(abc.ABC):

    ENTITY_TYPES: Dict[str, list]
    MEDIA_TYPES: list

    def __init__(self, artist_name: str, album_name: str):
        self.artist_name = artist_name.lower()
        self.album_name = album_name.lower()
        self.search_entity_type = None
        self.search_media_type = None

    def set_entity_type(self, value: str):
        if value not in self.ENTITY_TYPES.get(self.search_media_type, []):
            raise ValueError(f"Wrong entity type {value}")
        self.search_entity_type = value

    def set_media_type(self, value: str) -> None:
        if value not in self.MEDIA_TYPES:
            raise ValueError(f"Wrong media type {value}")
        self.search_media_type = value

    @abc.abstractmethod
    def prepare_request(self) -> dict:
        ...


class SearchEngineInterface(abc.ABC):

    def __init__(self):
        self.base_url = search_conf.search_url

    def execute(self, element: SearchElementInterface):
        result = requests.get(self.base_url, **element.prepare_request())
        print(result.request.url)
        return self.handle_result(result.text)

    @abc.abstractmethod
    def handle_result(self, result: str):
        ...
