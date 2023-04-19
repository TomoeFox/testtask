import abc

from config.storage import storage_conf


class DataStorageInterface(abc.ABC):

    def __init__(self):
        self.url = storage_conf.storage_url

    @abc.abstractmethod
    def save(self, data):
        ...
