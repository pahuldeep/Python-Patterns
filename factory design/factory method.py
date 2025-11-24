import json
import yaml
import xml.etree.ElementTree as ET

class JSONExtractor: 
    def __init__(self, file_path):
        self.data = {}
        with open(file_path, 'r') as file:
            self.data = json.load(file)

    @property
    def get_data(self):
        return self.data
        
class XMLExtractor: 
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        
    @property
    def get_data(self):
        return self.tree
        
class YAMLExtractor:
    def __init__(self, file_path):
        self.data = {}
        with open(file_path, 'r') as file:
            self.data = yaml.safe_load(file)
    
    @property
    def get_data(self):
        return self.data

def dataextractor(file_path):
    if file_path.endswith('.json'):
        extractor = JSONExtractor
    elif file_path.endswith('.xml'):
        extractor = XMLExtractor
    elif file_path.endswith('.yaml'):
        extractor = YAMLExtractor
    else:
        raise ValueError("Invalid file extension")
    return extractor(file_path)

def extract_data(file_path):
    factory_object = None
    try:
        factory_object = dataextractor(file_path)
    except ValueError as e:
        print(e)

    return factory_object

def main():
    factory = extract_data('dummy_data/person.sql')
    
    factory = extract_data('factory design/dummy_data/electronics.json')
    json_data = factory.get_data

    factory = extract_data('factory design/dummy_data/vehicles.xml')
    xml_data = factory.get_data

    factory = extract_data('factory design/dummy_data/animals.yaml')
    yaml_data = factory.get_data

    print(f'\nFound: {len(json_data)} items')
    print(f'\nFound: {len(xml_data.findall(f'.//vehicles'))} items')
    print(f'\nFound: {len(yaml_data)} items')
    print("*"*75)

    for i, device in enumerate(json_data["electronics"]):
        print(f"Device {i+1}:")
        for key, value in device.items():
            print(f"  {key}: {value}")
        print()
    print("*"*75)

    for vehicle in xml_data.findall('.//vehicle'):  # Using XPath
        print(f"Vehicle Type: {vehicle.get('type')}")
        for child in vehicle:
            print(f"  {child.tag}: {child.text}")
        print()
    print("*"*75)

    for i, names in enumerate(yaml_data['animals']):
        print(f"Animal {i+1}:")
        for key, value in names.items():
            print(f"  {key}: {value}")
        print()
    print("*"*75)


if __name__ == '__main__':
    main()

