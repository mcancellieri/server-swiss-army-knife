import xml.dom.minidom as minidom

def getName(self):
    return "XML"

def getDescription(self):
    return "Pretty print an XML"

def convert(self, stringToConvert):
    stringToConvert = stringToConvert.replace("\\n","")
    stringToConvert = stringToConvert.replace("\\","")
    stringToConvert = minidom.parseString(stringToConvert)
    output = stringToConvert.toprettyxml(indent='    ')
    return output
