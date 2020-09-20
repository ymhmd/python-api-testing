import json


class ReadFiles:
    def read_json_file(self, file_path):
        with open(file_path) as json_file:
            return json.load(json_file)
