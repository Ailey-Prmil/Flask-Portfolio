from typing import Any
from yaml import safe_load, dump

class File_Manager:
    def __init__(self, target_field, file_path="portfolio/input.yaml"):
        self.target_field = target_field
        self.file_path = file_path

    def rewrite_file(func):
        def wrapper(self,*args, **kwargs):
            with open (self.file_path, "r") as file:
                file_data = safe_load(file)
            func(self,file_data=file_data,*args, **kwargs)
            with open (self.file_path, "w") as file:
                dump(file_data, file, sort_keys=False)
        return wrapper
    
    @rewrite_file
    def save_new_data(self, file_data):
        file_data[self.target_field.title] = self.target_field()

    @rewrite_file
    def append_data(self, file_data):
        file_data[self.target_field.title] = self.target_field.add_data(file_data[self.target_field.title])
 
    @rewrite_file
    # this function only be used in list fields
    def delete_data(self, file_data, deleted_data):
        for (index, data) in enumerate(file_data[self.target_field.title]):
            if data == deleted_data:
                file_data[self.target_field.title].pop(index)
                break

    def read_data(self):
        with open (self.file_path, "r") as file:
            file_data = safe_load(file)
            return file_data[self.target_field.title]







