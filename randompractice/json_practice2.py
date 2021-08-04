import json

# this is how you load json files into python
# we are getting the json from the mydata file, and we are creating a dictionary of the json object
with open('mydata.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object['people'][1])
