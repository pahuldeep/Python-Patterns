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

def display_data(data_type, data):
    if data_type == 'json':
        for i, device in enumerate(data['electronics']):
            print(f"Device {i+1}:")
            for key, value in device.items():
                print(f"  {key}: {value}")
            print()
        print("*"*75)
    
    elif data_type == 'xml':
        for vehicle in data.findall('.//vehicle'):  
            print(f"Vehicle Type: {vehicle.get('type')}")
            for child in vehicle:
                print(f"  {child.tag}: {child.text}")
            print()
        print("*"*75)
    
    elif data_type == 'yaml':
        for i, names in enumerate(data['animals']):
            print(f"Animal {i+1}:")
            for key, value in names.items():
                print(f"  {key}: {value}")
            print()
        print("*"*75)
    
    else:
        print("Unsupported data type")