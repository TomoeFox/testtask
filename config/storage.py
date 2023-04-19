from pydantic.config import BaseConfig
from pydantic import FilePath


class DataStorage(BaseConfig):
    storage_url: FilePath


storage_conf = DataStorage()
