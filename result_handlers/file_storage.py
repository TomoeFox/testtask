from . import DataStorageInterface


class FileDataStorage(DataStorageInterface):

    def __init__(self):
        super().__init__("file_storage_url")

    def save(self, data: list, name: str = None):
        if not name:
            raise ValueError("Specify file name")
        with open(f"{self.url}/{name}", "w") as file:
            file.writelines(data)


