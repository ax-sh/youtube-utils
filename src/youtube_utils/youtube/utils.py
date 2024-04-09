import json

from pathlib import Path


def write_json(self, data):
    with self.open('w', encoding='utf-8') as w:
        json.dump(data, w)


def read_json(self):
    with self.open('r', encoding='utf-8') as r:
        return json.load(r)


Path.write_json = write_json
Path.read_json = read_json