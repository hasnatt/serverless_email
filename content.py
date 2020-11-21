from jinja2 import Environment, FileSystemLoader
from datetime import date

today = date.today()
d = today.strftime("%d/%m/%Y")

# put data into dictinary
name = 'hasnat'
body = {
    'name': name,
    'date': d
}

# open file env and render emplate with dictionary
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('template.html')
HTML_CONTENT = template.render(body=body)
print(HTML_CONTENT)

# save the html
# with open("email.html", "w") as fh:
#     fh.write(output_from_parsed_template)