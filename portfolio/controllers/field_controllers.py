from abc import ABC, abstractmethod

class Field(ABC):
    title = None
    data = None
    @abstractmethod
    def __init__(self, title, data):
        pass

    @abstractmethod
    def add_data(self, original_file_data):
        pass

    def __str__(self):
        return str({self.title: self.data})
    
    def __call__(self):
        return {self.data}
class ListField(Field): # jobtitles and skill_tags are list fields
    def __init__(self, title, data):
        self.title = title
        if (type(data) == list):
            self.data = data
        else:
            self.data = data.split(";")

    def add_data(self, original_file_data):
        if original_file_data:
            original_file_data.extend(self.data)
        else :
            original_file_data = self.data
        return original_file_data
 
class StringField(Field): #full_name, contact.fields, about_me are string fields
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def add_data(self, original_file_data):
        self.data = ' '.join(filter(None,[original_file_data, self.data]))
        return self.data


class DictField(Field): #contact is a dictionary field
    data = {}
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def add_data(self, original_file_data):
        return (original_file_data) # no need to add data to dictionary field
    
    def get_keys(self):
        return list(self.data.keys())
    
    def set_field(self, field, value):
        if field in self.get_keys():
            self.data[field] = value
        else:
            raise ValueError("Invalid field name")
