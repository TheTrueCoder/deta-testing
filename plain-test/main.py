from json import dumps
def app(event):
    return dumps({"message": "Hello, world!"})
