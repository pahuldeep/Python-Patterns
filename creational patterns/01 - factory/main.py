from factory import extract_data, display_data
import os 

def main():
    # so when you need that thing, you ask the right worker for it - not the general manager!
    source_path = os.getcwd() + '/data/'

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


    # For data
    display_data('json', json_data)
    display_data('xml', xml_data)
    display_data('yaml', yaml_data)


if __name__ == '__main__':
    main()
