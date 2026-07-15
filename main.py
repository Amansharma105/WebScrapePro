import typer
from analysis.price_analysis import analyze_prices

app = typer.Typer()


@app.command()
def start():
    print("WebScrapePro is running!")


@app.command()
def scrape():
    print("Scraping product data...")


@app.command()
def report():
    print("Generating report...")


@app.command()
def analyze():
    prices = [49999, 47999, 48999, 46999]

    result = analyze_prices(prices)

    print(result)


@app.command()
def chart():
    print("Generating price charts...")


@app.command()
def alert():
    print("Sending price alerts...")


@app.command()
def dashboard():
    print("Launching dashboard...")


@app.command()
def html():
    print("Generating HTML report...")


@app.command()
def schedule():
    print("Scheduler started...")


@app.command()
def test():
    print("Running tests...")


if __name__ == "__main__":
    app()
