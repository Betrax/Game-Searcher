d1 = {"value": 2, "Name": "two"}, {"value": 3, "Name": "three"}, {"value": 1, "Name": "one"}

d2 = {"value": 1, "Name": "one"}, {"value": 2, "Name": "two"}, {"value": 3, "Name": "three"}, {"value": 4, "Name": "four"}

d2 = sorted(d1, key=lambda x: x["value"])

print(d2[0]["value"])

