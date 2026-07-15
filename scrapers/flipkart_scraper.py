from .base_scraper import BaseScraper


class FlipkartScraper(BaseScraper):

    def get_product(self, url):
        soup = self.fetch_page(url)

        if soup is None:
            return None

        title = soup.find("span", class_="VU-ZEz")

        if title is None:
            title = soup.find("h1")

        price = soup.find("div", class_="Nx9bqj")

        product = {
            "title": title.get_text(strip=True) if title else "Not Found",
            "price": price.get_text(strip=True) if price else "Not Found",
            "website": "Flipkart"
        }

        return product
