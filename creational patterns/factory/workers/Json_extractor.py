import json

class JSONExtractor: 
    def __init__(self, file_path):
        self.data = {}
        with open(file_path, 'r') as file:
            self.data = json.load(file)

    @property
    def get_data(self):
        return self.data