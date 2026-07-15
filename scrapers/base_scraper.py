import requests
from bs4 import BeautifulSoup


class BaseScraper:

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )
        }

    def fetch_page(self, url):
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )

            response.raise_for_status()

            return BeautifulSoup(
                response.text,
                "html.parser"
            )

        except Exception as e:
            print(f"Error: {e}")
            return None
