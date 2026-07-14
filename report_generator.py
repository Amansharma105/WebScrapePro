from jinja2 import Template

def generate_report():

    with open("templates/report.html", "r") as file:
        template = Template(file.read())

    return template.render()
