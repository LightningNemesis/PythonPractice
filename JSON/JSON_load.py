import json

# We are going to convert Python:Dict -> JSON:object (called "Serialization")

person = {
    "name": "Bob",
    "age": 30,
    "hasChildren": False,
    "titles": [
        "App Developer",
        "Full Stack Developer",
        "PS Engineer"
    ]
}

# dumps, since we dump into a "string"
personJSON = json.dumps(person, indent=2, sort_keys=True)  # type: str

# person = json.loads(personJSON)
# print(personJSON)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(type(person), person)
