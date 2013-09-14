import re

def getName(self):
    return "SOAP Log"

def getDescription(self):
    return "Clean lines of log and make them readable"

def convert(self, stringToConvert):
    purged = re.sub(re.compile('^.* SOAP (REQUEST|RESPONSE) \d+/\d+:\s', re.MULTILINE),'', str(stringToConvert))
    purged = purged.replace("\n","")
    purged = purged.replace("\\n","")
    purged = purged.replace("\\","")
    print purged
    purged = minidom.parseString(purged)
    output = purged.toprettyxml(indent='    ')
    return output



