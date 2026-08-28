import requests
import xml.etree.ElementTree as ET

url = "http://192.168.100.2:3000/rpc/get-interface-information"

response = requests.get(
    url,
    auth=("lab", "lab123")
)

root = ET.fromstring(response.text)

for interface in root.findall(".//physical-interface"):
    name = interface.find("name")

    if name is not None:
        print(name.text.strip())