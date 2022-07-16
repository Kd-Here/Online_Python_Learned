# Json is notation/type makes data sharing easy between client to server and server to client.


import json

# some JSON:
xa = '{ "name":"John", "age":30, "city":"New York"}'

# parse x: from json to python dict
ya = json.loads(xa)

# the result is a Python dictionary:
print(ya)


xb= {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON: from py dict to json obj
yb = json.dumps(xb)

# the result is a JSON string:
print(yb)


# Suppose we had an real world scenario where we are storing names and details about people

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 30", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))
