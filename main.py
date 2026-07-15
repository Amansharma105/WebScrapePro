import typer
from scrapers.scraper import scrape_products
from analysis.analysis import analyze_prices
from alerts.email_alert import send_alert
from dashboard.dashboard import launch_dashboard
from reports.report_generator import generate_report
from scheduler.scheduler import start_scheduler

app = typer.Typer(help="WebScrapePro - E-Commerce Price Tracker")


@app.command()
def start():
    """Start the application"""
    print("🚀 WebScrapePro Started Successfully")


@app.command()
def scrape():
    """Scrape product prices"""
    scrape_products()


@app.command()
def analyze():
    """Analyze scraped prices"""
    analyze_prices()


@app.command()
def report():
    """Generate HTML Report"""
    generate_report()


@app.command()
def alert():
    """Send Email Alert"""
    send_alert()


@app.command()
def dashboard():
    """Launch Dashboard"""
    launch_dashboard()


@app.command()
def schedule():
    """Start Scheduler"""
    start_scheduler()


@app.command()
def all():
    """Run Complete Workflow"""
    print("========== WebScrapePro ==========")
    scrape_products()
    analyze_prices()
    generate_report()
    send_alert()
    print("✅ Project Completed Successfully")


if __name__ == "__main__":
    app()
