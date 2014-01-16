import xml.etree.ElementTree as etree

class Field:
    def __str__(self):
        return self.name

    def __init__(self, name='', expectedvalue=''):
        self.name = name
        self.expectedvalue = expectedvalue


def createfieldfromdictionnary(dictfield):
    newfield = Field()
    if 'name' in dictfield:
        newfield.name = dictfield['name']

    if 'eval' in dictfield:
        newfield.expectedvalue = dictfield['eval']

    return newfield


def createfieldfromxml(node):
    newfield = Field()
    valobj = None

    valobj = node.find("name")
    if valobj is not None:
        newfield.name = valobj.text

    valobj = node.find("expectedValue")
    if valobj is not None:
        newfield.expectedvalue = valobj.text

    return newfield