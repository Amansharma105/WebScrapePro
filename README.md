# WebScrapePro

WebScrapePro is a Python-based Command Line Interface (CLI) application for tracking product prices from e-commerce websites. It helps users monitor product prices, analyze trends, store product information, generate reports, and manage price alerts.

---

## Features

- CLI using Typer
- Product price scraping
- Amazon scraper
- Flipkart scraper
- HTML parsing using BeautifulSoup
- SQLite database integration
- Product storage
- Product model
- Price analysis
- Lowest, highest, and average price calculation
- Line chart generation
- Bar chart generation
- Price trend visualization
- HTML report generation
- Jinja2 template support
- Streamlit dashboard
- Product statistics
- Dashboard metrics
- Email alert system
- Automatic price checking
- APScheduler integration
- Scheduled tasks
- Automated testing with Pytest

---

## Project Structure

```text
WebScrapePro/
│
├── data/
│   └── .gitkeep
│
├── scrapers/
│   ├── .gitkeep
│   ├── base_scraper.py
│   ├── amazon_scraper.py
│   └── flipkart_scraper.py
│
├── database/
│   ├── .gitkeep
│   └── product_repository.py
│
├── analysis/
│   ├── .gitkeep
│   ├── price_analysis.py
│   └── price_chart.py
│
├── dashboard/
│   ├── .gitkeep
│   └── app.py
│
├── templates/
│   ├── .gitkeep
│   └── report.html
│
├── alerts/
│   ├── .gitkeep
│   └── email_alert.py
│
├── tests/
│   ├── .gitkeep
│   └── test_main.py
│
├── main.py
├── config.py
├── database.py
├── models.py
├── scheduler.py
├── report_generator.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Technologies Used

- Python
- Typer
- Requests
- BeautifulSoup4
- SQLite
- SQLAlchemy
- Pandas
- Matplotlib
- Jinja2
- Streamlit
- APScheduler
- Pytest

---
## Future Improvements

- Support for more e-commerce websites
- Interactive dashboard
- Real-time price alerts
- Email notifications
- Export reports to PDF and Excel
- Advanced price analytics

## Author

### Aman Sharma
