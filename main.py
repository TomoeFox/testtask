import argparse

from search_engine.itunes import ItunesMediaTypes, ItunesEntityTypes, ItunesSearchEngine, ItunesSearchElement, \
    ItunesAttributeTypes
from search_engine.chordify import ChordifySearchEngine, ChordifySearchElement
from result_handlers.csv_storage import CSVDataStorage
from result_handlers.file_storage import FileDataStorage


parser = argparse.ArgumentParser(
                    prog='Music Helper',
                    description='Helps get all album songs by one specified song or get chords for song'
)

parser.add_argument('-m', "--mode",
                    type=str,
                    required=True,
                    help="songs or chord modes only",
                    choices=["song", "chord"]
                    )
parser.add_argument('-a', '--author',
                    required=True,
                    type=str)
parser.add_argument('-s', '--song',
                    required=True,
                    type=str)

args = parser.parse_args()

if args.mode == "song":

    storage = CSVDataStorage()

    search_eng = ItunesSearchEngine()
    search_element_song = ItunesSearchElement(args.author, args.song)
    search_element_song.set_media_type(ItunesMediaTypes.MUSIC)
    search_element_song.set_entity_type(ItunesEntityTypes.SONG)
    search_element_song.set_attribute_type(ItunesAttributeTypes.ALBUM_TERM)

    search_result = search_eng.execute(search_element_song)
    results = search_result["results"]
    album_name = None
    album_name_reserved = None
    for result in results:
        artist = result["artistName"].lower()
        if artist == search_element_song.artist_name:
            if "single" in result["collectionName"].lower():
                album_name_reserved = result["collectionName"]
            else:
                album_name = result["collectionName"]

    if not (album_name or album_name_reserved):
        raise ValueError("Album not found")
    search_element_album = ItunesSearchElement(args.author, album_name or album_name_reserved)
    search_element_album.set_media_type(ItunesMediaTypes.MUSIC)
    search_element_album.set_entity_type(ItunesEntityTypes.SONG)
    search_result_album = search_eng.execute(search_element_album)

    prepared_results = []
    for result in search_result_album["results"]:
        if (album_name or album_name_reserved).lower() in result["collectionName"].lower():
            prepared_results.append(result)

    storage.save(prepared_results)
elif args.mode == "chord":
    file_storage = FileDataStorage()

    chordify_search = ChordifySearchEngine()
    chordify_element = ChordifySearchElement(args.author, args.song)
    chord_result = chordify_search.execute(chordify_element)
    file_storage.save(chord_result, name=f"{args.author} - {args.song}")
