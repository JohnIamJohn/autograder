import xml.etree.ElementTree as etree
from field import *

tr = etree.parse('./ex001.xml')
rt = tr.getroot()

Fields = []
for node in rt:
    newNode = createfieldfromxml(node)
    print str(newNode)
    Fields.append(newNode)
