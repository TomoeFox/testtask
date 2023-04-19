import json

from . import SearchEngineInterface, SearchElementInterface


class ItunesMediaTypes:

    MOVIE: str = "movie"
    PODCAST: str = "podcast"
    MUSIC: str = "music"
    MUSIC_VIDEO: str = "musicVideo"
    AUDIOBOOK: str = "audiobook"
    SHORT_FILM: str = "shortFilm"
    TV_SHOW: str = "tvShow"
    SOFTWARE: str = "software"
    EBOOK: str = "ebook"
    ALL: str = "all"


class ItunesEntityTypes:

    SONG: str = "song"


class ItunesAttributeTypes:

    ALBUM_TERM = "albumTerm"


class ItunesSearchElement(SearchElementInterface):

    MEDIA_TYPES = [ItunesMediaTypes.ALL, ItunesMediaTypes.EBOOK, ItunesMediaTypes.MUSIC, ItunesMediaTypes.MUSIC_VIDEO,
                   ItunesMediaTypes.MOVIE, ItunesMediaTypes.AUDIOBOOK, ItunesMediaTypes.PODCAST,
                   ItunesMediaTypes.SHORT_FILM, ItunesMediaTypes.SOFTWARE, ItunesMediaTypes.TV_SHOW]

    ENTITY_TYPES = {
        ItunesMediaTypes.MUSIC: [ItunesEntityTypes.SONG]
    }

    ATTRIBUTE_TYPES = {
        ItunesEntityTypes.SONG: [ItunesAttributeTypes.ALBUM_TERM]
    }

    def prepare_request(self) -> dict:
        params = {}
        if self.search_media_type:
            params["media"] = self.search_media_type or ItunesMediaTypes.ALL
        if self.search_entity_type:
            params["entity"] = self.search_entity_type
        params["term"] = f"{self.artist_name} {self.value}"
        return {"params": params}


class ItunesSearchEngine(SearchEngineInterface):

    def __init__(self):
        super().__init__("itunes_search_url")

    def handle_result(self, result: str):
        json_data = json.loads(result)
        return json_data
