"""Seralize and deserialize python object"""
import pprint
import jsonpickle


def serialize(obj, file_path, is_printing=False):
    "Serialize python object and save as json"
    with open(file_path, 'w') as inf:
        json_obj = jsonpickle.encode(obj)
        if is_printing:
            pprint.pprint(json_obj)
        inf.write(json_obj)


def deserialize(file_path):
    "Deserialize json to python object"
    with open(file_path, 'r') as outf:
        json_str = outf.read()
        obj = jsonpickle.decode(json_str)
        return obj
