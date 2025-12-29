from workers.Json_extractor import JSONExtractor
from workers.xml_extractor import XMLExtractor
from workers.yaml_extractor import YAMLExtractor
        
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


