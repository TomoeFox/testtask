import os

from csv import DictWriter

from . import DataStorageInterface


class CSVDataStorage(DataStorageInterface):

    def __init__(self):
        super().__init__("csv_storage_url")

    FIELDNAMES = ['artistId', 'collectionId', 'trackId', 'artistName', 'collectionName',
                  'trackName', 'collectionCensoredName', 'trackCensoredName', 'artistViewUrl',
                  'collectionViewUrl', 'trackViewUrl', 'previewUrl',
                  'collectionPrice', 'trackPrice', 'releaseDate', 'discCount',
                  'discNumber', 'trackCount', 'trackNumber', 'trackTimeMillis', 'country',
                  'currency', 'primaryGenreName']

    def save(self, data: list):
        file_path = f"{self.url}/result.csv"
        is_file_exists = os.path.exists(file_path)
        with open(file_path, "a+") as file:

            writer = DictWriter(file, fieldnames=self.FIELDNAMES)
            if not is_file_exists:
                writer.writeheader()

            prepared_data = []
            for element in data:
                necessary_keys = set(self.FIELDNAMES).intersection(set(element))
                prepared_data.append(
                    {key: element[key] for key in necessary_keys}
                )
            writer.writerows(prepared_data)

