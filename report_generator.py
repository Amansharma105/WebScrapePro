from datetime import datetime

def generate_report(products):
    report = []
    report.append("WEBSCRAPEPRO PRICE REPORT")
    report.append("=" * 40)
    report.append(f"Generated: {datetime.now()}")
    report.append("")

    for product in products:
        report.append(f"Product : {product['name']}")
        report.append(f"Price   : ₹{product['price']}")
        report.append("-" * 40)

    return "\n".join(report)
