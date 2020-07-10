import json

x = '{"name":"Ashik", "Age":25, "Profession": "Student"}'

y = json.loads(x)
print(y["Age"])
