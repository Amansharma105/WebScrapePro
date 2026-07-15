class Product:

    def __init__(self, title, price, website):

        self.title = title

        self.price = price

        self.website = website

    def __str__(self):

        return f"{self.title} - {self.price} ({self.website})"
