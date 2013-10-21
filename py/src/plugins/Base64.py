import base64

def getName(self):
    return "Base64"

def getDescription(self):
    return "Convert a Base64 string to readable text"

def convert(self, stringToConvert):
    output = base64.b64decode(stringToConvert)
    return output

