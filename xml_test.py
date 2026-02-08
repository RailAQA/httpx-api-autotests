import xml.etree.ElementTree as ET

data = """
<user>
    <name>Igor</name>
</user>   

"""

test_data = ET.fromstring(data)
print(test_data.find('user'))
