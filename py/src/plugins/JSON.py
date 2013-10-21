import json

def getName(self):
    return "JSON"

def getDescription(self):
    return "Pretty print a JSON string"

def convert(self, stringToConvert):
    textJ = json.loads(unicode(str(stringToConvert), errors='replace'))
    output = str(json.dumps(textJ, indent=4))
    return output
