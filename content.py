# from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('template.html')


output_from_parsed_template = template.render(name='Hasnat!')
print(output_from_parsed_template)

# to save the results
with open("email.html", "w") as fh:
    fh.write(output_from_parsed_template)