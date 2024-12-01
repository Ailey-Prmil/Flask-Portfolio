from .field_controllers import StringField, DictField, ListField

class FullName (StringField):
    def __init__(self, data):
        super().__init__("full_name", data)
class JobTitle (ListField):
    def __init__(self, data):
        super().__init__("job_titles", data)

class SkillTag (ListField):
    def __init__(self, data):
        super().__init__("skill_tags", data)
class AboutMe (StringField):
    def __init__(self, data):
        super().__init__("about_me", data)

class Section (ListField):
    def __init__(self, title):
        self.title = title
        self.data = []
    def build_data(self, new_data, Component):
        for component in new_data:
            new_component = Component(component)
            self.data.append(new_component)
    def add_data(self, original_file_data):
        data = [component.data for component in self.data]
        if original_file_data:
            original_file_data.extend(data)
        else:
            original_file_data = data
        return original_file_data
    def __call__(self):
        return [component.data for component in self.data]

# contact field
class Contact (DictField):
    keys = ["email", "facebook", "github", "linkedin", "location", "phone"]
    def __init__(self):
        self.title = "contact"
        for key in self.keys:
            self.data[key] = None

# config field
class Config (DictField):
    keys = ["about_me", "achievements", "certificates", "educations", "experiences", "projects"]
    def __init__(self):
        self.title = "config"
        for key in self.keys:
            self.data[key] = False
    def set_field(self, *fields):
        for field in fields:
            if field in self.keys:
                self.data[field] = True
            else:
                raise ValueError("Invalid field name")

class EduComponent (DictField):
    keys = ["date", "school", "description"]
    def __init__(self, data):
        super().__init__("education-component", data)

class Education (Section):
    def __init__(self):
        super().__init__("educations")

    def build_data(self, new_data):
        super().build_data(new_data, Component=EduComponent)
    

class ExperienceComponent (DictField):
    keys = ["date", "title", "company", "skills_included", "description"]
    def __init__(self, data):
        super().__init__("experience-component", data)

class Experience (Section):
    def __init__(self):
        super().__init__("experiences")

    def build_data(self, new_data):
        super().build_data(new_data, Conponent=ExperienceComponent)

class ProjectComponent (DictField):
    keys = ["title", "date", "reference", "skills_included", "description", "details"]
    def __init__(self, data):
        super().__init__("project-component", data)
    
class Project (Section):
    def __init__(self):
        super().__init__("projects")

    def build_data(self, new_data):
        super().build_data(new_data, Component=ProjectComponent)

class CertificateComponent (DictField):
    keys = ["title", "date", "issuer", "reference"]
    def __init__(self, data):
        super().__init__("certificate-component", data)
class Certificate (Section):
    def __init__(self):
        super().__init__("certificates")

    def build_data(self, new_data):
        super().build_data(new_data, CertificateComponent)

class SoftSkillComponent (DictField):
    keys = ["name", "description"]
    def __init__(self, data):
        super().__init__("soft-skill-component", data)

class SoftSkill (Section):
    def __init__(self):
        super().__init__("Soft_Skills")
    def build_data(self, new_data):
        super().build_data(new_data, SoftSkillComponent)

class HardSkillComponent (DictField):
    keys = ["name", "description", "tag"]
    def __init__(self, data):
        super().__init__("hard-skill-component", data)

class HardSkill(Section):
    def __init__(self):
        super().__init__("Hard_Skills")
    def build_data(self, new_data):
        super().build_data(new_data, HardSkillComponent)

class Skill(DictField):
    keys = ["Hard_Skills", "Soft_Skills"]
    component = {}
    def __init__(self):
        self.title = "skills"
        self.data["Hard_Skills"] = HardSkill()
        self.data["Soft_Skills"] = SoftSkill()

    def build_data(self, new_data):
        for key in self.keys:
            self.data[key].build_data(new_data[key])
    def add_data(self, original_file_data):
        for key in self.keys:
            original_file_data[key] = self.data[key].add_data(original_file_data[key])
        return original_file_data
    def __call__(self):
        return {key: self.data[key]() for key in self.keys}
