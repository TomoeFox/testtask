from pydantic import BaseSettings
from pydantic import HttpUrl


class SearchEngine(BaseSettings):

    itunes_search_url: HttpUrl
    chordify_search_url: HttpUrl


search_conf = SearchEngine()
