# WebScrapePro

WebScrapePro is a Python-based Command Line Interface (CLI) application that tracks product prices from e-commerce websites. It collects product information, stores data in a SQLite database, analyzes price trends, generates reports, visualizes data, and supports automated monitoring.

---

## Features

- Command Line Interface using Typer
- Product Price Scraping
- Amazon Product Scraper
- Flipkart Product Scraper
- HTML Parsing with BeautifulSoup
- SQLite Database Integration
- Product Repository Management
- Product Data Model
- Price Analysis
- Lowest, Highest and Average Price Calculation
- Price Trend Analysis
- Bar Chart Generation
- Line Chart Generation
- HTML Report Generation
- Jinja2 Template Rendering
- Streamlit Dashboard
- Dashboard Metrics
- Email Alert System
- APScheduler Integration
- Automated Testing using Pytest

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

## Requirements

- Python 3.11+
- Git
- Requests
- BeautifulSoup4
- Pandas
- SQLAlchemy
- Matplotlib
- Jinja2
- Streamlit
- APScheduler
- Pytest
  
## Author

### Aman Sharma
