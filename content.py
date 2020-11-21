from jinja2 import Environment, FileSystemLoader

# put data into dictinary
name = 'hasnat'
body = {
    'name': name
}

# open file env and render emplate with dictionary
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('template.html')
HTML_CONTENT = template.render(body=body)
print(HTML_CONTENT)

# save the html
# with open("email.html", "w") as fh:
#     fh.write(output_from_parsed_template)