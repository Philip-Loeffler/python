import json


mydict = {
    "people": [
        {
            "name": "Bob",
            "age": 28,
            "weight": 80
        },
        {
            "name": "Anna",
            "age": 30,
            "weight": 70
        },
        {
            "name": "phil",
            "age": 31,
            "weight": 170
        },
        {
            "name": "charles",
            "age": 36,
            "weight": 140
        }
    ]
}

# json.dumps takes a json object and turns it into a string
json_string = json.dumps(mydict, indent=2)
# this will write our json string into a json file
with open("mydata.json", "w") as f:
    f.write(json_string)
