from pydantic import BaseSettings
from pydantic import FilePath, DirectoryPath


class DataStorage(BaseSettings):
    csv_storage_url: DirectoryPath
    file_storage_url: DirectoryPath


storage_conf = DataStorage()
