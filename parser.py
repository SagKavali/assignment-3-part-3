import xml.etree.ElementTree as ET
root = ET.parse('./note.xml').getroot()

print(root)

for item in root:
    print(item)