import typer

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

if __name__ == "__main__":
    app()
