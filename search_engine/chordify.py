import bs4

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from . import SearchEngineInterface, SearchElementInterface


class ChordifySearchElement(SearchElementInterface):

    def prepare_request(self) -> str:
        return f"{self.artist_name}-songs/{self.value}-chords".replace(" ", "-")


class ChordifySearchEngine(SearchEngineInterface):

    def __init__(self):
        super().__init__("chordify_search_url")

    def execute(self, element: ChordifySearchElement):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        try:
            driver.get(f"{self.base_url}/{element.prepare_request()}")

            return self.handle_result(driver.page_source)
        finally:
            driver.close()

    def handle_result(self, result: str):
        soup = bs4.BeautifulSoup(result, features="html.parser")
        result = []
        for chord in soup.findAll(class_="chord"):

            if "data-i" not in chord.attrs:
                continue
            line_id = chord.attrs["data-i"]
            label = chord.find(class_="chord-label")
            chord_type = label.attrs["class"][-1].rsplit("-")[-1]
            result.append(f"{line_id} {chord_type}\n")
        return result


