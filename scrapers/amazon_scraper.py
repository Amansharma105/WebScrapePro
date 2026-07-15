from .base_scraper import BaseScraper


class AmazonScraper(BaseScraper):

    def get_product(self, url):
        soup = self.fetch_page(url)

        if soup is None:
            return None

        title = soup.find("span", id="productTitle")

        price = (
            soup.find("span", class_="a-price-whole")
            or soup.find("span", class_="a-offscreen")
        )

        product = {
            "title": title.get_text(strip=True) if title else "Not Found",
            "price": price.get_text(strip=True) if price else "Not Found",
            "website": "Amazon"
        }

        return product
