from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

def addhearts(text):
    return f"\U00002764  {text} \U00002764 "
env.filters["addhearts"] = addhearts

template = env.get_template("email.template.txt")

data = {
    "name": "Bruno",
    "products": [
        {"name": "iphone", "price": 13000.320},
        {"name": "ferrari", "price": 900000.430}
    ],
    "special_customer": True,
}

print(template.render(**data))