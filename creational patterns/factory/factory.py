# The Factory Method is like a specialized worker who ONLY knows how to make ONE type of thing, 
# Each factory worker makes ONE type of thing - that's the power!

from data_machine import DataExtractorFactory

def extract_data(file_path):
    try:
        extractor = DataExtractorFactory.create_extractor(file_path)
        return extractor
    except ValueError as e:
        print(e)
        return None


def display_json_data(json_data):
    for i, device in enumerate(json_data['electronics']):
        print(f"Device {i+1}:")
        for key, value in device.items():
            print(f"  {key}: {value}")
        print()
    print("*"*75)

def display_xml_data(xml_data):
    for vehicle in xml_data.findall('.//vehicle'):  
        print(f"Vehicle Type: {vehicle.get('type')}")
        for child in vehicle:
            print(f"  {child.tag}: {child.text}")
        print()
    print("*"*75)

def display_yaml_data(yaml_data):
    for i, names in enumerate(yaml_data['animals']):
        print(f"Animal {i+1}:")
        for key, value in names.items():
            print(f"  {key}: {value}")
        print()
    print("*"*75)
    

def main():
    # so when you need that thing, you ask the right worker for it - not the general manager!
    source_path = 'creational patterns/factory/data/'

    json_factory = extract_data(source_path + 'electronics.json')   # JSON Factory creates JSON data
    yaml_factory = extract_data(source_path + 'animals.yaml')       # YAML Factory creates YAML data
    xml_factory = extract_data(source_path + 'vehicles.xml')        # XML Factory creates XML data  

    if json_factory: 
        json_data = json_factory.get_data
        print(f'Found: {len(json_data["electronics"])} items')

    if xml_factory: 
        xml_data = xml_factory.get_data
        print(f'Found: {len(xml_data.findall(".//vehicle"))} items')

    if yaml_factory:
        yaml_data = yaml_factory.get_data
        print(f'Found: {len(yaml_data["animals"])} items')
    print("#"*75)

    display_json_data(json_data)
    display_xml_data(xml_data)
    display_yaml_data(yaml_data)



if __name__ == '__main__':
    main()
