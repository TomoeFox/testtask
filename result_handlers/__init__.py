import abc

from config.storage import storage_conf


class DataStorageInterface(abc.ABC):

    def __init__(self, param_name):
        self.url = getattr(storage_conf, param_name, None)

    @abc.abstractmethod
    def save(self, data):
        ...
