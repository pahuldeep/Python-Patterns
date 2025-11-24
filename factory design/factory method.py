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

# THE FACTORY FACTORY - IT CREATES THE RIGHT FACTORY
class DataExtractorFactory:
    @staticmethod
    def create_extractor(file_path):
        if file_path.endswith('.json'):
            return JSONExtractor(file_path)  # Returns a JSON factory
        elif file_path.endswith('.xml'):
            return XMLExtractor(file_path)   # Returns an XML factory  
        elif file_path.endswith('.yaml'):
            return YAMLExtractor(file_path)  # Returns a YAML factory
        else:
            raise ValueError("Invalid file extension")

def extract_data(file_path):
    try:
        extractor = DataExtractorFactory.create_extractor(file_path)
        return extractor
    except ValueError as e:
        print(e)
        return None


def main():
    # Each factory makes ONE type of thing - that's the power!
    json_factory = extract_data('factory design/dummy_data/electronics.json')   # JSON Factory creates JSON data
    if json_factory:
        json_data = json_factory.get_data
        print(f'Found: {len(json_data["electronics"])} items')


    xml_factory = extract_data('factory design/dummy_data/vehicles.xml')    # XML Factory creates XML data  
    if xml_factory:
        xml_data = xml_factory.get_data
        print(f'Found: {len(xml_data.findall(".//vehicle"))} items')


    yaml_factory = extract_data('factory design/dummy_data/animals.yaml')   # YAML Factory creates YAML data
    if yaml_factory:
        yaml_data = yaml_factory.get_data
        print(f'Found: {len(yaml_data["animals"])} items')
    print("*"*75)


    # "The Factory Method is like a specialized worker who ONLY knows how to make ONE type of thing, 
    #  so when you need that thing, you ask the right worker for it - not the general manager!"
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

