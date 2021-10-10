import json

data = """
{
    "name":"Chuck",
    "phone":{
        "type":"intl",
        "number":"+7630306"
    },
    "email":{
        "hide":"yes"
    }
}
"""

info = json.loads(data)
print(info["name"])
print("Hide:", info["email"]["hide"])