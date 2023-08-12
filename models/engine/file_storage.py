#!/usr/bin/python3

"""Model for serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json


class FileStorage:
    """Class File Storage

        Attributes:
            __file_path (str): path to the JSON file
            __objects (obj): store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[id] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        objs = {}
        for key, val in FileStorage.__objects.items():
            objs[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                load_objs = json.load(f)

            for key, val in load_objs.items():
                FileStorage.__objects[key] = eval(val['__class__'])(**val)
        except FileNotFoundError:
            pass
