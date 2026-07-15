def get_lowest_price(prices):
    return min(prices)


def get_highest_price(prices):
    return max(prices)


def get_average_price(prices):
    return round(sum(prices) / len(prices), 2)


def analyze_prices(prices):

    return {
        "Lowest Price": get_lowest_price(prices),
        "Highest Price": get_highest_price(prices),
        "Average Price": get_average_price(prices)
    }
