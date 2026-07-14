import matplotlib.pyplot as plt

def line_chart(prices):
    plt.plot(prices)
    plt.title("Price Trend")

def bar_chart(products, prices):
    plt.bar(products, prices)
    plt.title("Product Prices")
