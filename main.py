import typer

from database import create_table
from analysis.price_analysis import analyze_prices

app = typer.Typer()


@app.command()
def start():
    create_table()
    print("Database Ready")
    print("WebScrapePro Started Successfully")


@app.command()
def scrape():
    print("Scraping Product Data...")


@app.command()
def analyze():

    prices = [49999, 47999, 48999, 46999]

    result = analyze_prices(prices)

    print("\nAnalysis Result")
    print("----------------")

    for key, value in result.items():
        print(f"{key}: {value}")


@app.command()
def report():
    print("Generating HTML Report...")


@app.command()
def dashboard():
    print("Launching Dashboard...")


@app.command()
def alert():
    print("Checking Price Alerts...")


@app.command()
def schedule():
    print("Scheduler Started...")


@app.command()
def chart():
    print("Generating Charts...")


@app.command()
def test():
    print("Running Tests...")


if __name__ == "__main__":
    app()
