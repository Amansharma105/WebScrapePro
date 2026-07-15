from jinja2 import Environment, FileSystemLoader


def generate_report(products):

    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template("report.html")

    html = template.render(products=products)

    with open("reports/report.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("HTML Report Generated Successfully")
