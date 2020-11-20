from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(''))
template = env.get_template('template.html')
HTML_CONTENT = template.render(name='Hasnat!')
print(HTML_CONTENT)

# to save the results
# with open("email.html", "w") as fh:
#     fh.write(output_from_parsed_template)