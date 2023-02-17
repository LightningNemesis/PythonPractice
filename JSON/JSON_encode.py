from json import JSONEncoder
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


# We need to encode the data type "User" into a (class Dict)
def encode_user(obj):
    if isinstance(obj, User):
        return {
            "name": obj.name,
            "age": obj.age, obj.__class__.__name__: True
        }
    else:
        raise TypeError("Object of type User is not JSON serializable")


class UserEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, User):
            return {
                "name": obj.name,
                "age": obj.age, obj.__class__.__name__: True
            }
        return JSONEncoder.default(self, obj)

# Way 1:
# userJSON = json.dumps(user, default=encode_user)  # Dumping as a JSON string

# Way 2:
# userJSON = json.dumps(user, cls=UserEncoder)  # Dumping as a JSON string


# Way 3:
userJSON = UserEncoder().encode(user)

print(userJSON)
