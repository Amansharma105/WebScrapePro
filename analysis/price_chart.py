import matplotlib.pyplot as plt


def line_chart(prices):

    plt.figure(figsize=(8,4))

    plt.plot(prices, marker="o")

    plt.title("Price Trend")

    plt.xlabel("Days")

    plt.ylabel("Price")

    plt.grid(True)

    plt.savefig("data/line_chart.png")

    plt.close()


def bar_chart(products, prices):

    plt.figure(figsize=(8,4))

    plt.bar(products, prices)

    plt.title("Product Prices")

    plt.savefig("data/bar_chart.png")

    plt.close()
