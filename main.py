from search_engine.itunes import ItunesMediaTypes, ItunesEntityTypes, ItunesSearchEngine, ItunesSearchElement
from result_handlers.csv_storage import CSVDataStorage

search_eng = ItunesSearchEngine()
search_element = ItunesSearchElement("Paradise Lost", "Tragic Idol")
search_element.set_media_type(ItunesMediaTypes.MUSIC)
search_element.set_entity_type(ItunesEntityTypes.SONG)
search_result = search_eng.execute(search_element)
storage = CSVDataStorage()
storage.save(search_result["results"])

