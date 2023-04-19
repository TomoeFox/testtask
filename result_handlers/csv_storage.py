from csv import DictReader, DictWriter

from . import DataStorageInterface


class CSVDataStorage(DataStorageInterface):

    def save(self, data: list):
        with open(self.url, "r+") as file:
            reader = DictReader(file)
            formatted_fieldnames = [fieldname.strip().strip("'") for fieldname in reader.fieldnames]

            writer = DictWriter(file, fieldnames=formatted_fieldnames)

            prepared_data = []
            for element in data:
                necessary_keys = set(formatted_fieldnames).intersection(set(element))
                prepared_data.append(
                    {key: element[key] for key in necessary_keys}
                )
            writer.writerows(prepared_data)

