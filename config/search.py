from pydantic.config import BaseConfig
from pydantic import HttpUrl


class SearchEngine(BaseConfig):

    search_url: HttpUrl


search_conf = SearchEngine()
