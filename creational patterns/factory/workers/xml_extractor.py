import xml.etree.ElementTree as ET

class XMLExtractor: 
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        
    @property
    def get_data(self):
        return self.tree